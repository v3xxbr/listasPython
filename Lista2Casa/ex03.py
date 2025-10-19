media = float(input('Digite a média: '))
media = round(media,2)
dec = media - int(media)

media=int(media)

if (dec*100) > 50:
    media+=1

print(f'A média arredondada é {media:.2f}')