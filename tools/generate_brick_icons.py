#!/usr/bin/env python3
"""Deterministic BrickForge 3D-style icon asset generator (original artwork).
Produces 512px icons and validates mapped resources; no initials/monograms.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, json, xml.etree.ElementTree as ET

ROOT=Path("app/src/main/res")
DEST=ROOT/"drawable-nodpi"
SIZE=512
CATALOG={
"uber":("car",(20,20,24)),
"tasks":("checklist",(38,126,222)),
"peacock":("fan",(42,60,113)),
"photos":("flower",(255,255,255)),
"smartthings":("house",(38,136,212)),
"ebay":("cart",(234,203,40)),
"google_earth":("globe",(23,95,173)),
"suno":("music",(25,25,32)),
"newegg":("egg",(222,114,40)),
"steam_link":("controller",(27,46,75)),
"plague_inc":("virus",(86,43,90)),
"costco":("store",(193,43,45)),
"maps":("pin",(51,157,99)),
"gallery":("landscape",(132,75,198)),
"facebook":("social",(25,100,207)),
"disney_plus":("castle",(22,43,117)),
"assistant":("spark",(36,135,221)),
"translate":("translate",(28,116,207)),
"ups":("shield",(111,63,30)),
"discover":("card",(37,42,48)),
}
# Confirm package names and launcher component mappings on a device before publishing.
PACKAGES={
"com.ubercab":"uber",
"com.google.android.apps.tasks":"tasks",
"com.google.android.apps.photos":"photos",
"com.samsung.android.oneconnect":"smartthings",
"com.ebay.mobile":"ebay",
"com.google.earth":"google_earth",
"com.valvesoftware.steamlink":"steam_link",
"com.google.android.apps.maps":"maps",
"com.facebook.katana":"facebook",
"com.google.android.apps.translate":"translate",
}
def lighter(c,amount):return tuple(min(255,int(x+(255-x)*amount)) for x in c)
def darker(c,amount):return tuple(max(0,int(x*(1-amount))) for x in c)
def rect(d,b,c,r=10):d.rounded_rectangle(b,radius=r,fill=c)
def ellipse(d,b,c):d.ellipse(b,fill=c)
def poly(d,points,c):d.polygon(points,fill=c)
def icon(name,kind,color):
    im=Image.new("RGBA",(SIZE,SIZE),(0,0,0,0))
    shadow=Image.new("RGBA",(SIZE,SIZE),(0,0,0,0))
    sd=ImageDraw.Draw(shadow)
    sd.rounded_rectangle((34,62,485,484),radius=79,fill=(0,0,0,125))
    shadow=shadow.filter(ImageFilter.GaussianBlur(13))
    im.alpha_composite(shadow)
    d=ImageDraw.Draw(im)
    rect(d,(24,45,484,474),darker(color,.40),80)
    rect(d,(24,35,478,459),color,77)
    d.arc((29,40,473,455),185,315,fill=lighter(color,.58),width=10)
    d.arc((31,42,475,458),5,140,fill=darker(color,.42),width=11)
    # Brick grid seams and a physically raised pair of top studs.
    for y in (180,320):
        d.line((42,y,458,y),fill=darker(color,.28),width=5)
        d.line((42,y+5,458,y+5),fill=lighter(color,.22),width=3)
    for x in (164,327):
        d.line((x,185,x,438),fill=darker(color,.24),width=4)
    for x in (133,371):
        ellipse(d,(x-51,52,x+51,153),darker(color,.35))
        ellipse(d,(x-51,39,x+51,140),lighter(color,.25))
        d.arc((x-48,42,x+48,137),190,330,fill=lighter(color,.75),width=7)
    # Raised emblem plate with directional bevel.
    rect(d,(78,189,433,429),darker(color,.42),46)
    rect(d,(75,178,425,416),lighter(color,.09),43)
    d.arc((79,183,420,411),190,320,fill=lighter(color,.55),width=7)
    # Emblem is rendered on its own layer and extruded.
    symbol=Image.new("RGBA",(SIZE,SIZE),(0,0,0,0))
    q=ImageDraw.Draw(symbol)
    white=(248,250,253,255); dark=(21,29,43,255)
    if kind=="car":
        rect(q,(128,277,383,371),white,22);poly(q,[(178,277),(212,232),(309,232),(344,277)],white)
        for x in (184,327):ellipse(q,(x-26,351,x+26,403),dark)
        rect(q,(215,247,303,278),(77,162,226),7)
    elif kind=="checklist":
        rect(q,(146,217,366,397),white,15)
        for y in (261,319,377):
            q.line([(165,y),(179,y+13),(206,y-13)],fill=(27,149,90),width=12)
            q.line((230,y,340,y),fill=(45,110,207),width=11)
    elif kind=="fan":
        for i,c in enumerate(((225,47,55),(241,139,36),(244,207,54),(38,177,85),(37,123,217),(131,77,207))):
            x=120+i*44;ellipse(q,(x,230+int(abs(i-2.5)*12),x+75,345),c)
        ellipse(q,(236,294,280,388),white)
    elif kind=="flower":
        for x,y,c in ((211,245,(230,67,57)),(283,245,(247,194,44)),(211,317,(49,162,89)),(283,317,(42,125,226))):
            ellipse(q,(x-43,y-43,x+43,y+43),c)
        ellipse(q,(230,264,275,309),white)
    elif kind=="house":
        poly(q,[(126,290),(256,206),(386,290),(386,399),(126,399)],white)
        rect(q,(229,314,284,399),(39,127,202),6)
        q.arc((184,236,329,327),205,335,fill=dark,width=10)
    elif kind=="cart":
        q.line([(134,246),(170,246),(197,364),(352,364),(375,278),(188,278)],fill=white,width=17)
        for x in (222,328):ellipse(q,(x-21,377,x+21,419),white)
        for x,c in ((230,(221,61,53)),(273,(45,165,92)),(315,(241,196,56))):rect(q,(x-19,251,x+19,302),c,3)
    elif kind=="globe":
        ellipse(q,(151,218,361,428),(41,126,212))
        poly(q,[(172,255),(228,226),(268,272),(326,283),(306,346),(252,329),(220,404),(180,350)],(49,165,95))
        q.arc((155,223,356,423),70,290,fill=white,width=7)
    elif kind=="music":
        q.arc((151,219,363,388),182,357,fill=white,width=24)
        rect(q,(132,316,171,388),white,12);rect(q,(345,316,384,388),white,12)
        q.line((264,263,264,358),fill=white,width=16)
        q.line((264,263,328,246),fill=white,width=16)
        ellipse(q,(217,345,274,388),white)
    elif kind=="egg":
        ellipse(q,(142,223,371,409),white)
        ellipse(q,(192,238,327,397),(238,154,47))
        ellipse(q,(220,252,305,374),lighter((238,154,47),.35))
    elif kind=="controller":
        rect(q,(137,267,374,371),white,48)
        q.line((188,302,188,352),fill=dark,width=15);q.line((165,327,212,327),fill=dark,width=15)
        for x,y in ((311,305),(339,329),(309,353)):ellipse(q,(x-10,y-10,x+10,y+10),(39,119,213))
    elif kind=="virus":
        ellipse(q,(176,241,338,402),(235,224,232))
        for a in range(0,360,45):
            x=257+int(109*math.cos(math.radians(a)));y=320+int(109*math.sin(math.radians(a)))
            q.line((257,320,x,y),fill=white,width=10)
            ellipse(q,(x-13,y-13,x+13,y+13),white)
        for x,y in ((226,301),(288,301),(258,352)):ellipse(q,(x-11,y-11,x+11,y+11),(133,50,108))
    elif kind=="store":
        rect(q,(146,276,368,405),white,9)
        for i in range(5):
            rect(q,(145+i*45,250,190+i*45,290),(220,52,54) if i%2==0 else white,3)
        rect(q,(224,331,288,405),(34,110,206),3)
    elif kind=="pin":
        ellipse(q,(171,207,343,379),(225,53,60))
        poly(q,[(194,346),(320,346),(257,425)],(225,53,60))
        ellipse(q,(222,256,291,325),white)
    elif kind=="landscape":
        rect(q,(129,228,383,401),white,14)
        rect(q,(148,247,364,381),(48,139,209),5)
        ellipse(q,(292,263,342,313),(249,207,65))
        poly(q,[(148,381),(224,291),(275,350),(317,319),(364,381)],(48,162,93))
    elif kind=="social":
        rect(q,(177,214,336,411),white,22)
        q.line((277,236,246,266,246,388),fill=(31,101,210),width=26)
        q.line((212,302,299,302),fill=(31,101,210),width=25)
    elif kind=="castle":
        q.arc((124,224,390,390),190,355,fill=white,width=10)
        poly(q,[(151,395),(151,313),(188,313),(188,274),(218,274),(218,341),(246,341),(246,247),(279,247),(279,330),(309,330),(309,289),(347,289),(347,395)],white)
    elif kind=="spark":
        for a in range(0,360,45):
            x=257+int(105*math.cos(math.radians(a)));y=315+int(105*math.sin(math.radians(a)))
            q.line((257,315,x,y),fill=white,width=15)
        ellipse(q,(229,287,285,343),white)
    elif kind=="translate":
        rect(q,(127,229,294,386),white,13)
        q.line((170,274,254,274),fill=(28,105,210),width=10)
        q.line((211,246,211,334),fill=(28,105,210),width=10)
        rect(q,(254,293,391,409),(25,111,215),12)
        q.line((283,351,358,351),fill=white,width=10)
        q.line((318,324,318,381),fill=white,width=9)
    elif kind=="shield":
        poly(q,[(151,229),(363,229),(348,364),(257,423),(166,364)],(100,58,32))
        q.line([(166,240),(348,240),(336,354),(257,407),(178,354),(166,240)],fill=(240,186,52),width=12)
        poly(q,[(257,263),(285,306),(333,309),(297,339),(306,387),(257,361),(207,387),(217,339),(180,309),(229,306)],(240,186,52))
    elif kind=="card":
        rect(q,(128,246,385,394),dark,16)
        rect(q,(128,280,385,310),(42,139,222),0)
        ellipse(q,(265,330,329,387),(227,83,48))
        ellipse(q,(304,330,369,387),(241,192,52))
    alpha=symbol.getchannel("A")
    raised=Image.new("RGBA",(SIZE,SIZE),(0,0,0,0))
    shade=Image.new("RGBA",(SIZE,SIZE),(7,12,20,175))
    raised.paste(shade,(0,0),alpha)
    raised=raised.transform((SIZE,SIZE),Image.Transform.AFFINE,(1,0,-9,0,1,-10))
    im.alpha_composite(raised)
    im.alpha_composite(symbol)
    d=ImageDraw.Draw(im)
    for y in (290,358):
        for x in (187,257,327):
            if alpha.getpixel((x,y))>180:
                ellipse(d,(x-7,y-7,x+7,y+7),(255,255,255,110))
                d.arc((x-8,y-8,x+8,y+8),10,150,fill=(25,25,25,90),width=2)
    return im
def main():
    DEST.mkdir(parents=True,exist_ok=True)
    for name,(kind,color) in CATALOG.items():
        icon(name,kind,color).save(DEST/("bf_"+name+".png"),optimize=True)
    root=ET.Element("resources")
    for package,name in PACKAGES.items():
        if name not in CATALOG:raise ValueError(name)
        ET.SubElement(root,"item",component=f"ComponentInfo{{{package}/}}",drawable="bf_"+name)
    ET.indent(root,space="    ")
    (ROOT/"xml").mkdir(parents=True,exist_ok=True)
    ET.ElementTree(root).write(ROOT/"xml"/"appfilter.xml",encoding="unicode",xml_declaration=True)
    draw=ET.Element("resources");cat=ET.SubElement(draw,"category",title="BrickForge")
    for name in CATALOG:ET.SubElement(cat,"item",drawable="bf_"+name)
    ET.indent(draw,space="    ")
    ET.ElementTree(draw).write(ROOT/"xml"/"drawable.xml",encoding="unicode",xml_declaration=True)
    Path("icon-report.json").write_text(json.dumps({"icons":len(CATALOG),"mapped_packages":len(PACKAGES),"unmapped_icons":sorted(set(CATALOG)-set(PACKAGES.values()))},indent=2))
    print(f"Generated {len(CATALOG)} brick icons, {len(PACKAGES)} package mappings")
if __name__=="__main__":main()
