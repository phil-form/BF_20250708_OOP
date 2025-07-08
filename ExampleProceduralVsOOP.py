from Models.ChatOOP import Chat
from Models.ChatProcedural import chat_meow, chat_create_cat, chat_eat
from Models.SousDossier.SousSousDossier.SuperFicherSecret import super_secret_function

cat = Chat("Mittens")

cat.meow()


cat = chat_create_cat("Mittens")
chat_eat(cat)
# import Models.ChatOOP as ChatOOP
#
# cat = ChatOOP.Chat("Mittens")

# import Models.ChatProcedural
# Models.ChatProcedural.chat_meow(cat)

import Models.ChatProcedural as ChatProcedural
ChatProcedural.chat_meow(cat)
ChatProcedural.chat_eat(cat)

import Models.SousDossier.main as SousDossierMain

SousDossierMain.second_main()
