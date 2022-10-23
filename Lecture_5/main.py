# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(4)) 




from turtle import update
from telegram import Update
from telegram.ext import  CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = update().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()