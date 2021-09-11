1 x=rnd(-ti)
2 cls$=chr$(147):print cls$
3 poke 53280,peek(53281)
5 input "vuoi le istruzioni";q$
6 if left$(q$,1)<>"n" then goto 300
7 print cls$;
9 x=rnd(-ti)
10 forx=1 to 16+rnd(1)*4:a$=a$+"Q":next
15 print cls$;
20 print a$+str$(len(a$))
30 input "quante palline prendi";p
35 if(p>3)or(p<1)thengoto30
40 a$=left$(a$,len(a$)-p)
45 if len(a$)<=0then goto 100
50 print a$+str$(len(a$))
55 c=len(a$)-int(len(a$)/4)*4
70 if c=0 then c=1+int(rnd(1)*2)
80 a$=left$(a$,len(a$)-c)
82 print"io ne prendo";int(c)
90 if len(a$)<=0then goto 200
94 goto 20
99 end
100 print"hai vinto!!!"
150 goto 250
200 print"ho vinto io!!!"
250 print:input"giochiamo ancora";q$
255 print cls$;
260 ifleft$(q$,1)<>"n"then goto 7
265 print:print"ciao!"
270 end
300 print cls$+" istruzioni:"
310 print"a turno ogni giocatore puo' prendere"
320 print"da una a tre palline"
330 print"vince chi prende l'ultima, le ultime due o le ultime tre!"
340 print:input" giochiamo";q$
350 goto 260

run
