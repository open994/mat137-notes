import json
import subprocess
import tempfile
import os

IDS = {
    "Chapter 1": ["4ca1t9noMlo","GQfOWN76eTA","XHapWWI_wJ8","h1milgIk4U8","4UwhnYJVi0o","WLI1yzvK_5w","VPzlj_OJyU0","PfAr1hhhL9o","H7NkSHt5Bao","IBwDUEXM0xs","9rYcAygjOas","a0_dQgwuzYk","x0d3gO1e868","NmgABEiwgLg","WPP2TDPXyc8"],
    "Chapter 2": ["UDGVvSXHLTQ","bo2YmvSaTNI","299WBtK_qro","6wFC38rVMbk","eCBM1tVHDqo","QNuoKYCO-mM","-oq8jPI74tY","29jRJO_QSW4","VOEzUbNTCSk","nUepIw5kC2s","p8Ox1LtXyCA","7TGgWs_qCWY","vTonfq94c8s","iF9F1qHTRdM","TtdsCGP-MAY","y1WYANJ7IPc","fLSQwA5gKT4","fXjZADF6HUo","8kogZvSk2S4","odRR5XVqHe8","r5Tz0wi5RRU","ncR9x7p6LaU"],
    "Chapter 3": ["7vhux5TLRmQ","eNcg9cKzV1Q","fUjLN1ZEDBc","k_VxtK1U9jk","QQbiHHiqTXo","GwxWAJP77ZY","4k2gpNW0pEw","7su5mypmgdw","QBmUyi64zf8","Qht28m7b13U","DQiXqChpeAc","E_Cvb53vXI0","Ce44nuJzzdw"],
    "Chapter 4": ["17lUN_X8vAY","DxecWsEms_c","bnsVbyLUZqs","BMXesqZ_XCA","q19VQuujeAI","FQHvMifuXHU","Nx7noVPMkXE","GLc0JgegIH4","0iF8AUWVrb0","kkEIHByB158","IJ6FwlnRSws","V7cK2SQMizE","kuKrSTOKw30","kANSILD9sn0"],
    "Chapter 5": ["heqUCdcgVYA","_z8OglXFIq8","SWb2T0ad6lw","_giwkVIFeGY","n8Nhn7N_rkE","5TKUOC06JzM","DKFV3KMDKHc","xL5qJSZie5Y","l10mJLuG-U4","15-oyDZT2aE","HlzVrFcqi04","HsMHLIwKmFo"],
    "Chapter 6": ["TjW3e01KW8M","DyoVgunLR18","AuWxVJPU0SI","SaeGMaz0w5g","yz8uZbi2wEk","6YvN79aDbjs","aaee9hSP7Gw","bbBaiKaCiE0","TMlnlD4HCrA","3EyFtXgJXTg","I7LjiDDI7ZA","ySxaqDTcWgk","4Dh6KdQDRkw","ZodaIjLuhI8","PG41kUSC0w0","gzoTke-bby4","UTFOz-4GZYs","5Obe9JUFtEg"],
    "Chapter 7": ["F9lfbCaXOpk","hZXPAEeu5D4","4qNstDwlh9I","YgXv698pN8g","dZ_TWQbksbg","Ev2w9NYqNvc","si1Ds7TrP14","N1R26svx9ZA","l_iMH_naiTo","k_DPWyRU2Rw","Hco-2q2A_ss"],
    "Chapter 8": ["xcyL3sEL2mM","BQIiCjoFILs","JeKCipoy8bc","UZmMgSIgi3k","OKw2v0DOXOI","58VnS2eczss","LBhvzrRyAtk"],
    "Chapter 9": ["6IiHC3-E3kQ","dS50LonV_ms","9WkYb_fRoG0","taKIe3Ui3oI","15DJgDvMpTE","gR-chzRVpWo","8TCGSagLskc","zrPCAP9-0wo","OT5DTVFfvFA","w-T90XSM90s","XwuohSB1e5w","NjmH5KjYS2k"],
    "Chapter 10": ["Kq9Q5LISo5o","YYM9URJ4iJ8"],
    "Chapter 11": ["utfrtw-H9-Q","Dr8LzBA-H84","xuNRMkzSzZY","J8uZJ9by0ys","njHTdc0rv6Y","5m7XdA7ogEk","Dd3n2rfqxf4","aMZRptPCtZc"],
    "Chapter 12": ["NqxwJ2D-Ckc","L9wxtktioik","pbr8GWBmLhU","LVKdfkNyp58","l0bYj2g9qqM","WAhjLIfNnjI","8xtCdrLzQpQ","9NeR7QXGJbE","2hOr_4hc3pA","FqJSWNtT_aA"],
    "Chapter 13": ["vJCGp9luzlc","VccmKguRkeY","OfDw7AoVXYs","jrO276f_wwg","IjTJP3ssOkk","x8zxHukU-UE","9njCb8usB94","kP9qHkTSNpI","_7qwFfSjBtE","spg7c-LY59o","bmb_K39nay0","QbYK4COJUqU","OM9U6Pwze8E","NFhV-ZVg6pg","2i0iUwLwwxs","_CSvVbH-0c0","H6f9mfqzeBg","2Fj56wxfLEo","S0C0XoEKGCk"],
    "Chapter 14": ["CYAPZikmuM4","IEH7d9XiqqA","aCFR5CABSA0","sNWY1w8YocM","c-rI1zMj0wA","o-RSENE_Yus","SXLJOa1_GMs","lQH-pqS7vdk","ksKu5p2qvB4","NYVjEbpY21w","vM7sLZ2ljko","4Gbmp8Qn8Xo","-CK3K_aeH64","ajglGMrE5Gk","1dSWYQ9AXuo"]
}

def fetch_transcript(video_id, tmpdir):
    subprocess.run([
        "yt-dlp",
        "--write-sub",
        "--sub-lang", "en-CA,en",
        "--sub-format", "json3",
        "--skip-download",
        "--no-warnings",
        "-o", os.path.join(tmpdir, "%(id)s"),
        f"https://www.youtube.com/watch?v={video_id}",
    ], check=True, capture_output=True)

    subtitle_path = None
    for lang in ("en-CA", "en"):
        candidate = os.path.join(tmpdir, f"{video_id}.{lang}.json3")
        if os.path.exists(candidate):
            subtitle_path = candidate
            break

    if subtitle_path is None:
        print(f"  WARNING: no en-CA or en subtitles for {video_id}, skipping")
        return ""

    with open(subtitle_path) as f:
        data = json.load(f)

    lines = []
    for event in data.get("events", []):
        for seg in event.get("segs", []):
            text = seg.get("utf8", "").strip()
            if text:
                lines.append(text)

    return "\n".join(lines)

def main():
    transcripts = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        for chapter, video_ids in IDS.items():
            print(f"Fetching {chapter}...")
            trs = []
            for video_id in video_ids:
                print(f"  {video_id}")
                transcript = fetch_transcript(video_id, tmpdir)
                trs.append(transcript)
            transcripts[chapter] = trs
            with open("transcripts.json", "w") as f:
                json.dump(transcripts, f)


    print("Done.")

if __name__ == "__main__":
    main()
