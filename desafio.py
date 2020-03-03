trabalho_terca = False
trabalho_quinta = True

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("tv50={} tv32={} sorvete={} saudavel={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))