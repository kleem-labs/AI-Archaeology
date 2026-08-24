"""Build the clickable five-realm memory palace for Excavations 201–225."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_excavations_201_225 import REALMS, ROOT_MEMORY, ROWS, concept


ROOT = Path(__file__).parents[1]
OUTPUT = ROOT / "mathematical-roots"
URL = "https://kleem-labs.github.io/AI-Archaeology/mathematical-roots/"


def collect() -> dict:
    realms = []
    for realm in REALMS:
        roots = []
        for row in ROWS:
            if realm["start"] <= row.number <= realm["end"]:
                memory = ROOT_MEMORY[row.number]
                roots.append({
                    "number": row.number,
                    "name": concept(row),
                    "title": row.title,
                    "path": f"../excavations/{row.number:03d}-{row.slug}/README.md",
                    **memory,
                })
        realms.append({**realm, "roots": roots})
    return {"version": 1, "realms": realms, "root_count": len(ROOT_MEMORY)}


def readme(data: dict) -> str:
    lines = [
        "# The Living Undercroft of Mathematical Roots",
        "",
        "This is the cinematic memory palace for Excavations 201–225.",
        "",
        "Use it during the retrieval passage in [How to Master AI "
        "Archaeology](../HOW_TO_MASTER_THIS_BOOK.md).",
        "",
        f"[**Enter the living, clickable Undercroft →**]({URL})",
        "",
        "A root is remembered as a five-frame transformation:",
        "",
        "```text",
        "question → physical object → visible failure → transformation → memory seal",
        "```",
        "",
        "The page is useful without memorizing its labels. Choose a chamber, replay "
        "the five frames, close the page, and reconstruct the root from the physical "
        "object. Every final seal links to the complete excavation where the equation "
        "is derived operation by operation.",
        "",
        "## The five realms",
        "",
        "| Realm | Roots | Human power recovered |",
        "|---|---:|---|",
    ]
    for realm in data["realms"]:
        first = realm["roots"][0]
        lines.append(
            f'| **{realm["number"]} — {realm["name"]}** | '
            f'{len(realm["roots"])} | {realm["question"]} '
            f'[Begin with {first["name"]}]({first["path"]}) |'
        )
    lines.extend([
        "",
        "For the complete script-free map, memory sentences, and chapter links, use "
        "[The Mathematical Roots](../MATHEMATICAL_ROOTS.md).",
        "",
    ])
    return "\n".join(lines)


def html_page(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    template = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A cinematic memory palace for the mathematical roots beneath AI">
  <title>AI Archaeology — The Mathematical Undercroft</title>
  <style>
    :root{color-scheme:dark}
    *{box-sizing:border-box}
    body{margin:0;min-height:100vh;color:#f7efd9;background:#070914;font-family:Inter,ui-sans-serif,system-ui,sans-serif}
    button,a{font:inherit}
    button:focus-visible,a:focus-visible{outline:3px solid #f4cf75;outline-offset:3px}
    .palace{min-height:100vh;background:radial-gradient(circle at 50% 18%,#25305c 0,#10152d 35%,#070914 78%);overflow:hidden}
    .head{max-width:1180px;margin:auto;padding:34px 22px 16px;text-align:center}
    .kicker{color:#f4cf75;font-size:12px;letter-spacing:.18em;text-transform:uppercase}
    h1{margin:8px 0 10px;font:500 clamp(31px,5vw,58px) Georgia,serif}
    .subtitle{max-width:760px;margin:auto;color:#b9c3db;line-height:1.6}
    .realms{max-width:1180px;margin:10px auto 0;padding:12px 20px;display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
    .realm{min-height:68px;padding:10px;border:1px solid #344067;background:#10162e;color:#aeb9d2;border-radius:10px;cursor:pointer}
    .realm strong{display:block;color:inherit;font-family:Georgia,serif;font-size:15px;font-weight:500}
    .realm span{font-size:11px}
    .realm[aria-pressed="true"]{color:#fff5d6;border-color:#f4cf75;background:#27203a;box-shadow:0 0 25px #f4cf7524}
    .corridor{max-width:1180px;margin:auto;padding:8px 20px 18px;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:5px}
    .root-node{width:41px;height:41px;padding:0;border-radius:50%;border:1px solid #48547c;background:#111830;color:#ccd5ea;cursor:pointer;font-size:11px}
    .root-node[aria-pressed="true"]{border-color:#f4cf75;background:#f4cf75;color:#171122;box-shadow:0 0 22px #f4cf7566}
    .thread{width:18px;height:1px;background:#58617b}
    .stage-wrap{max-width:1060px;margin:auto;padding:0 20px 34px}
    .stage{position:relative;min-height:500px;border:1px solid #303a60;border-radius:24px;background:linear-gradient(145deg,#121a35e8,#090e20f2);box-shadow:0 28px 90px #0009;overflow:hidden}
    .stage:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 52%,#f4cf7512,transparent 38%);pointer-events:none}
    .location{position:relative;padding:20px 24px 12px;display:flex;justify-content:space-between;gap:15px;color:#aeb9d2;font-size:12px}
    .location strong{color:#f4cf75;font-weight:500}
    .scene{position:relative;min-height:300px;padding:18px clamp(24px,6vw,74px);display:grid;place-items:center;text-align:center}
    .frame-number{color:#f4cf75;font-size:12px;letter-spacing:.17em;text-transform:uppercase}
    .scene h2{max-width:760px;margin:13px auto;font:500 clamp(25px,4vw,43px) Georgia,serif;line-height:1.16}
    .scene p{max-width:760px;margin:0 auto;color:#c1cbe0;font-size:clamp(15px,2vw,19px);line-height:1.65}
    .sigil{width:112px;height:112px;margin:0 auto 18px;display:grid;place-items:center;border:1px solid #f4cf7566;border-radius:50%;background:radial-gradient(circle,#f4cf7538,#f4cf7506 65%);color:#f4cf75;font:500 39px Georgia,serif;box-shadow:0 0 50px #f4cf7522}
    .frames{position:relative;padding:16px 20px 20px;display:grid;grid-template-columns:repeat(5,1fr);gap:7px;border-top:1px solid #283253;background:#090f22aa}
    .frame{padding:10px 6px;border:0;border-radius:8px;background:#161d36;color:#9da9c2;cursor:pointer;font-size:12px}
    .frame[aria-pressed="true"]{background:#f4cf75;color:#171122}
    .under-stage{max-width:1060px;margin:15px auto 0;display:flex;align-items:center;justify-content:space-between;gap:14px;color:#aeb9d2}
    .seal{font-family:Georgia,serif;font-size:16px}
    .open{display:inline-block;padding:9px 13px;border-radius:999px;background:#f4cf75;color:#171122;text-decoration:none;font-size:12px;font-weight:700;white-space:nowrap}
    .help{max-width:900px;margin:0 auto;padding:0 20px 30px;text-align:center;color:#7f8aa5;font-size:12px}
    .shift .scene-copy{animation:move .32s ease}
    @keyframes move{from{opacity:.1;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
    @media(prefers-reduced-motion:reduce){.shift .scene-copy{animation:none}}
    @media(max-width:760px){.realms{grid-template-columns:1fr}.realm{min-height:auto}.stage{min-height:540px}.frames{grid-template-columns:1fr 1fr}.frame:last-child{grid-column:1/-1}.under-stage{align-items:flex-start;flex-direction:column}.location{flex-direction:column}.scene{min-height:330px}.thread{width:8px}}
  </style>
</head>
<body>
<main class="palace" id="palace">
  <header class="head">
    <div class="kicker">AI Archaeology · Volume VI</div>
    <h1>The Undercroft of Mathematical Roots</h1>
    <p class="subtitle">Walk five realms. In every chamber, an ordinary object fails, transforms, and leaves behind a mathematical promise you can recover without memorizing a definition.</p>
  </header>
  <nav class="realms" aria-label="Five mathematical realms"></nav>
  <nav class="corridor" aria-label="Root chambers in the selected realm"></nav>
  <section class="stage-wrap">
    <div class="stage" aria-live="polite">
      <div class="location"></div>
      <div class="scene"><div class="scene-copy"></div></div>
      <div class="frames" aria-label="Five memory frames"></div>
    </div>
    <div class="under-stage"><div class="seal"></div><a class="open">Open the complete excavation</a></div>
  </section>
  <p class="help">Begin with the question. Advance one frame at a time. After the memory seal, close the page and replay the object’s transformation without looking.</p>
</main>
<script>
(function(){
  var data=__DATA__;
  var root=document.getElementById("palace");
  var realmNav=root.querySelector(".realms");
  var corridor=root.querySelector(".corridor");
  var location=root.querySelector(".location");
  var copy=root.querySelector(".scene-copy");
  var frameNav=root.querySelector(".frames");
  var seal=root.querySelector(".seal");
  var open=root.querySelector(".open");
  var selectedRealm=0,selectedRoot=0,selectedFrame=0;
  var frameNames=["Question","Object","Failure","Transformation","Memory seal"];
  var sigils=["?","◯","×","→","◆"];
  function safe(value){var div=document.createElement("div");div.textContent=value;return div.innerHTML}
  function current(){return data.realms[selectedRealm].roots[selectedRoot]}
  function frameText(item,index){
    return [
      item.question,
      item.object,
      item.failure_image,
      item.transformation,
      item.sentence
    ][index]
  }
  function renderRealms(){
    realmNav.innerHTML=data.realms.map(function(realm,index){
      return '<button class="realm" type="button" aria-pressed="'+(index===selectedRealm)+'" data-realm="'+index+'"><span>Realm '+realm.number+'</span><strong>'+safe(realm.name)+'</strong></button>';
    }).join("");
    realmNav.querySelectorAll("button").forEach(function(button){
      button.addEventListener("click",function(){selectedRealm=Number(button.dataset.realm);selectedRoot=0;selectedFrame=0;render()});
    });
  }
  function renderCorridor(){
    var roots=data.realms[selectedRealm].roots;
    corridor.innerHTML=roots.map(function(item,index){
      var join=index?'<span class="thread" aria-hidden="true"></span>':"";
      return join+'<button class="root-node" type="button" aria-label="Excavation '+item.number+': '+safe(item.name)+'" aria-pressed="'+(index===selectedRoot)+'" data-root="'+index+'">'+item.number+'</button>';
    }).join("");
    corridor.querySelectorAll("button").forEach(function(button){
      button.addEventListener("click",function(){selectedRoot=Number(button.dataset.root);selectedFrame=0;render()});
    });
  }
  function renderFrames(){
    frameNav.innerHTML=frameNames.map(function(name,index){
      return '<button class="frame" type="button" aria-pressed="'+(index===selectedFrame)+'" data-frame="'+index+'">'+(index+1)+' · '+name+'</button>';
    }).join("");
    frameNav.querySelectorAll("button").forEach(function(button){
      button.addEventListener("click",function(){selectedFrame=Number(button.dataset.frame);renderScene()});
    });
  }
  function renderScene(){
    var realm=data.realms[selectedRealm],item=current();
    location.innerHTML='<span><strong>'+safe(realm.name)+'</strong> · '+safe(realm.path)+'</span><span>Excavation '+item.number+' · '+safe(item.name)+'</span>';
    copy.innerHTML='<div class="sigil" aria-hidden="true">'+sigils[selectedFrame]+'</div><div class="frame-number">Frame '+(selectedFrame+1)+' · '+frameNames[selectedFrame]+'</div><h2>'+safe(frameText(item,selectedFrame))+'</h2><p>'+(selectedFrame===4?safe(item.gesture):safe(realm.question))+'</p>';
    seal.textContent=selectedFrame===4?item.sentence:"Do not skip ahead; let the chamber change.";
    open.href=item.path;
    root.classList.remove("shift");void root.offsetWidth;root.classList.add("shift");
    renderFrames();
  }
  function render(){renderRealms();renderCorridor();renderScene()}
  render();
})();
</script>
</body>
</html>
'''
    return template.replace("__DATA__", payload)


def outputs() -> dict[Path, str]:
    data = collect()
    return {
        OUTPUT / "data.json": json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        OUTPUT / "README.md": readme(data),
        OUTPUT / "index.html": html_page(data),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = outputs()

    if args.check:
        stale = [
            str(path) for path, content in generated.items()
            if not path.exists() or path.read_text() != content
        ]
        if stale:
            raise SystemExit("Mathematical Roots palace is stale:\n" + "\n".join(stale))
        print("Mathematical Roots palace matches all 25 memory films.")
    else:
        OUTPUT.mkdir(exist_ok=True)
        for path, content in generated.items():
            path.write_text(content)
        print("Built the five-realm Mathematical Roots memory palace.")


if __name__ == "__main__":
    main()
