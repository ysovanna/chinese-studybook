# -*- coding: utf-8 -*-
"""Give every Khmer support line its own native voice clip (edge-tts km-KH, free, no key).

    python tools/gen_audio_km.py <unit-slug> [--voice km-KH-SreymomNeural]

Walks unit.json, collects every "km"/"akm" string that has no kmaudio/kaudio yet,
synthesises audio/kmNN.mp3 and writes the paths back. Safe to re-run: existing files kept.
"""
import asyncio
import io
import json
import os
import sys

import edge_tts

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    slug = sys.argv[1]
    d = os.path.join(ROOT, slug)
    path = os.path.join(d, 'unit.json')
    u = json.load(io.open(path, encoding='utf-8'))
    voice = sys.argv[sys.argv.index('--voice') + 1] if '--voice' in sys.argv else 'km-KH-SreymomNeural'

    jobs = []
    n = [0]

    def want(text, key_au):
        n[0] += 1
        au = f'audio/km{n[0]:02d}.mp3'
        return (text, au)

    for c in u['cards']:
        if c.get('km') and not c.get('kmaudio'):
            t, au = want(c['km'], 'kmaudio'); c['kmaudio'] = au; jobs.append((t, au))
        elif c.get('km') and c.get('kmaudio'):
            jobs.append((c['km'], c['kmaudio']))
    for b in u['qa']:
        for it in b['items']:
            if b.get('kind') == 'surv':
                if it.get('km') and not it.get('kmaudio'):
                    t, au = want(it['km'], 'kmaudio'); it['kmaudio'] = au; jobs.append((t, au))
                elif it.get('km') and it.get('kmaudio'):
                    jobs.append((it['km'], it['kmaudio']))
            else:
                if it.get('akm') and not it.get('kaudio'):
                    t, au = want(it['akm'], 'kaudio'); it['kaudio'] = au; jobs.append((t, au))
                elif it.get('akm') and it.get('kaudio'):
                    jobs.append((it['akm'], it['kaudio']))

    io.open(path, 'w', encoding='utf-8', newline='\n').write(json.dumps(u, ensure_ascii=False, indent=1))

    todo = [(t, os.path.join(d, a)) for t, a in jobs
            if not (os.path.exists(os.path.join(d, a)) and os.path.getsize(os.path.join(d, a)) > 800)]

    async def run():
        sem = asyncio.Semaphore(4)
        failed = []

        async def one(text, out):
            async with sem:
                os.makedirs(os.path.dirname(out), exist_ok=True)
                for attempt in range(3):
                    try:
                        await edge_tts.Communicate(text.replace("'", ''), voice, rate='-5%').save(out)
                        return
                    except Exception:
                        if attempt == 2:
                            failed.append((text, out))
                        else:
                            await asyncio.sleep(1.5 * (attempt + 1))
        await asyncio.gather(*(one(t, o) for t, o in todo))
        if failed:
            print('FAILED texts:')
            for t_, o_ in failed:
                print(' ', repr(t_), '->', os.path.basename(o_))

    asyncio.run(run())
    print(f'{slug}: {len(jobs)} khmer clips referenced, {len(todo)} generated with {voice}')


if __name__ == '__main__':
    main()
