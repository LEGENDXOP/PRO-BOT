from Luna import CMD_HELP
from Luna.events import register
from Luna import tbot, OWNER_ID
import os
from PIL import Image, ImageDraw, ImageFont

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 text = quew
 if event.sender_id == OWNER_ID:
     pass
 else:
     if event.is_group:
       await event.reply('Currently This Module Only Works in my [PM](tg://user?id=1624337697)')
       return
     else:
       pass
 if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
 else:
       pass
 await event.reply('Hnm.')
 
# get an image
 base = Image.open('./Luna/resources/photo_2021-03-18_10-37-51.jpg').convert('RGBA')
 txt = Image.new('RGBA', base.size, (255,255,255,0))
 font = ImageFont.truetype('./Luna/resources/Distort Me.otf', 160)
# get a drawing context
 d = ImageDraw.Draw(txt)

# draw text, half opacity
 d.text((80,490), text, font=font, fill=(240,248,255,128))
# draw text, full opacity
 d.text((70,450), text, font=font, fill=(255,255,255,255), stroke_width=6, stroke_fill="black")

 out = Image.alpha_composite(base, txt)
 fname = 'lel.png'
 out.save(fname, "png")
 await tbot.send_file(event.chat_id, fname, caption="Made By Anie")
 if os.path.exists(fname2):
            os.remove(fname2)

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 In Beta!.
 - /logo <text>
Module Not Finished.!
Send Logo Bgs and Fonts to Bot DM! will add to module.
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
