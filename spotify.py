# -*- coding: utf-8 -*-
import os

win_dir = 'C:\Windows\System32\Drivers\etc'
mac_dir = '/private/etc'
linux_dir = '/etc'


def main30():
    while True:
        print '1. Windows'
        print '2. Linux'
        print '3. Mac OS X 10.6 to 10.10'
        number = raw_input('Choose your operative system: ')
        number = number.rstrip()  # eliminamos espacios en blanco
        if not number.isdigit():
            print 'Write 1 or 2'
        elif int(number) != 1 and int(number) != 2 and int(number) != 3:
            print 'Are you kidding me?'
        else:
            break

    if int(number) == 1:  # seleccionamos el directorio correcto según nuestro SO
        my_dir = win_dir
    elif int(number) == 2:
        my_dir = linux_dir
    else:
        my_dir = mac_dir

    if os.path.isdir(my_dir):
        os.chdir(my_dir)  # cambiamos a este directorio de trabajo
        archivo = open("hosts", "r+")  # abrimos y añadimos nuevos hosts al archivo 'hosts'
        archivo.read()

        archivo.write("127.0.0.1 doubleclick.net\n")
        archivo.write("127.0.0.1 media-match.com\n")
        archivo.write("127.0.0.1 adclick.g.doublecklick.net\n")
        archivo.write("127.0.0.1 www.googleadservices.com\n")
        archivo.write("127.0.0.1 open.spotify.com\n")
        archivo.write("127.0.0.1 pagead2.googlesyndication.com\n")
        archivo.write("127.0.0.1 desktop.spotify.com\n")
        archivo.write("127.0.0.1 googleads.g.doubleclick.net\n")
        archivo.write("127.0.0.1 pubads.g.doubleclick.net\n")
        archivo.write("127.0.0.1 securepubads.g.doubleclick.net\n")
        archivo.write("127.0.0.1 audio2.spotify.com\n")
        archivo.write("127.0.0.1 www.omaze.com\n")
        archivo.write("127.0.0.1 omaze.com\n")
        archivo.write("127.0.0.1 bounceexchange.com\n")
        archivo.write("127.0.0.1 core.insightexpressai.com\n")
        archivo.write("127.0.0.1 content.bitsontherun.com\n")
        archivo.write("127.0.0.1 s0.2mdn.net\n")
        archivo.write("127.0.0.1 v.jwpcdn.com\n")
        archivo.write("127.0.0.1 d2gi7ultltnc2u.cloudfront.net\n")
        archivo.write("127.0.0.1 crashdump.spotify.com\n")
        archivo.write("127.0.0.1 adeventtracker.spotify.com\n")
        archivo.write("127.0.0.1 log.spotify.com\n")
        archivo.write("127.0.0.1 analytics.spotify.com\n")
        archivo.write("127.0.0.1 ads-fa.spotify.com\n")
        archivo.close()  # cerramos y notificamos
        print 'Yeah! Now You can listen to Spotify music as a premium user!'
    else:
        print 'Mate, You have selected a wrong operative system!'

if __name__ == '__main__':
    main30()
