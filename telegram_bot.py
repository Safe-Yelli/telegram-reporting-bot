import os

# Connect to google sheets
import gspread  
service_account = gspread.service_account(filename='key.json')
sheet = service_account.open("Multi platform data aggregation test")
worksheet = sheet.worksheet("Sheet1")
sheet_row = []

# Connect to telegram BOT 
# TOKEN = os.getenv("TOKEN")
print(os.getenv("TOKEN"))
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
print("Bot started.")

user_data = {
  "date" : "NA"
}

# Features of the telegram BOT
CHOOSING, TYPING_REPLY = range(2)

# Ways to arrange 6 buttons on the keyboard.
reply_keyboard = [["Date", "Time"], ["Location", "Category"], ["Description", "Done"]] # 6x2
# reply_keyboard = [["Date"], ["Time"], ["Location"], ["Category"], ["Description"], ["Done"]]  # 6x1

detail_list = ["Date", "Time", "Location", "Category", "Description"]
removed_list = []

# Opens the 6 button keyboard. Buttons are in the reply_keyboard list.
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


# Converting user input to str.
def details_to_str(user_data):
    """Helper function for formatting the gathered user info."""
    details = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(details).join(["\n", "\n"])

async def start_fn(update: Update, context: ContextTypes.DEFAULT_TYPE):
  for removed_item in removed_list:
    detail_list.append(removed_item)
  # print(detail_list)

  welcome_text = "Welcome to SafeYelli's Reporting BOT. Please provide information about the incident."
  await update.message.reply_text(welcome_text, reply_markup=markup)
  return CHOOSING

async def describe_fn(update: Update, context: ContextTypes.DEFAULT_TYPE):
  selected_detail = update.message.text
  context.user_data["choice"] = selected_detail
  await update.message.reply_text(f"You selected {selected_detail.lower()}. Type the {selected_detail.lower()} below.")
  return TYPING_REPLY
  await update.message.reply_text(f"Information given:\n {details_to_str(user_data)}\nEdit the information provided or Continue describing or press Done.", reply_markup=markup)
  return CHOOSING

async def received_information_fn(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_data = context.user_data
  selected_detail = update.message.text
  detail_key = user_data["choice"] # Whatever you choose on the markup keyboard becomes your choice.
  user_data[detail_key] = selected_detail
  del user_data["choice"]

  await update.message.reply_text(f"Information given:\n {details_to_str(user_data)}\nEdit the information provided or Continue describing or press Done.", reply_markup=markup)
  return CHOOSING

async def done_fn(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_data = context.user_data
  if "choice" in user_data:
      del user_data["choice"]

  await update.message.reply_text(f"Information given:\n {details_to_str(user_data)}\nThankyou for reporting!",
      reply_markup=ReplyKeyboardRemove())

  for key in user_data.keys():
    if key in detail_list:
      detail_list.remove(key)
      # print("removed " + key)
      removed_list.append(key)

  for detail in detail_list:
    user_data[detail] = "NA"

  for data in user_data.items():
    sheet_row.append(str(data))
  sheet_row.sort()
  worksheet.insert_row(sheet_row)

  sheet_row.clear()
  user_data.clear()
  return ConversationHandler.END

# Start the code

def main():
  application = Application.builder().token(TOKEN).build()

  main_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start_fn)],
    states={
      CHOOSING: [
        MessageHandler(filters.Regex("Date"), describe_fn),
        MessageHandler(filters.Regex("Time"), describe_fn),        
        MessageHandler(filters.Regex("Location"), describe_fn),        
        MessageHandler(filters.Regex("Category"), describe_fn),
        MessageHandler(filters.Regex("Description"), describe_fn),
      ],
      TYPING_REPLY: [MessageHandler(filters.TEXT and ~(filters.COMMAND or filters.Regex("Done")), received_information_fn)]},
    fallbacks=[MessageHandler(filters.Regex("Done"), done_fn)])

  application.add_handler(main_handler)
  application.run_polling()

###################################################################################################################

if __name__ == "__main__":
  while True:
    main()
