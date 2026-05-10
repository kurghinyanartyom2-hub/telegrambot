import os
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
    
)

խաղեր = {
    "Minecraft": {
        "գին": "5000 դրամ, կարող ես նաև քաշել անվճար տարբերակ",
        "ինֆորմացիա": "Minecraft-ում դու կարող ես գոյատևել բաց աշխարհում քո ընկերների հետ"
    },

    "CS GO": {
        "գին": "Անվճար է",
        "ինֆորմացիա": "CS GO-ն կրակոցային խաղ է"
    },

    "GTA V": {
        "գին": "8000 դրամ",
        "ինֆորմացիա": "GTA V-ը open-world խաղ է"
    },

    "It Takes Two": {
        "գին": "12000 դրամ",
        "ինֆորմացիա": "It Takes Two-ը co-op արկածային խաղ է երկու խաղացողի համար"
    },

    "PUBG Battlegrounds": {
        "գին": "Անվճար է",
        "ինֆորմացիա": "PUBG Battlegrounds-ը battle royale կրակոցային խաղ է"
    },
   
}

ծրագրեր = {
    "Photoshop": {
        "գին": "4000 դրամ",
        "ինֆորմացիա": "Photoshop-ը նկարների խմբագրման ծրագիր է"
    },

    "VS Code": {
        "գին": "Անվճար է",
        "ինֆորմացիա": "VS Code-ը ծրագրավորման editor է"
    },

    "Telegram": {
        "գին": "Անվճար է",
        "ինֆորմացիա": "Telegram-ը մեսենջեր է"
    }
}

հարցեր = [
    {
        "հարց": "Հայաստանի մայրաքաղաքը որն է",
        "տարբերակներ": ["Երևան", "Գյումրի", "Վանաձոր", "Կապան"],
        "ճիշտ": "Երևան",
        "գումար": "1000 դրամ"
    },

    {
        "հարց": "Որ մոլորակն է հայտնի Կարմիր մոլորակ անունով",
        "տարբերակներ": ["Երկիր", "Մարս", "Յուպիտեր", "Սատուրն"],
        "ճիշտ": "Մարս",
        "գումար": "5000 դրամ"
    },

    {
        "հարց": "Minecraft-ը որ թվականին ստեղծվեց",
        "տարբերակներ": ["2005", "2009", "2012", "2015"],
        "ճիշտ": "2009",
        "գումար": "10000 դրամ"
    },

    {
        "հարց": "Ով է ստեղծել Facebook-ը",
        "տարբերակներ": [
            "Bill Gates",
            "Elon Musk",
            "Mark Zuckerberg",
            "Steve Jobs"
        ],
        "ճիշտ": "Mark Zuckerberg",
        "գումար": "20000 դրամ"
    },

    {
        "հարց": "2-ի քառակուսին հավասար է",
        "տարբերակներ": ["2", "4", "6", "8"],
        "ճիշտ": "4",
        "գումար": "50000 դրամ"
    },

    {
        "հարց": "Աշխարհի ամենամեծ օվկիանոսը որն է",
        "տարբերակներ": [
            "Ատլանտյան",
            "Հնդկական",
            "Խաղաղ",
            "Սառուցյալ"
        ],
        "ճիշտ": "Խաղաղ",
        "գումար": "100000 դրամ"
    },

    {
        "հարց": "Python-ը ինչ է",
        "տարբերակներ": [
            "Խաղ",
            "Ծրագրավորման լեզու",
            "Համակարգիչ",
            "Բրաուզեր"
        ],
        "ճիշտ": "Ծրագրավորման լեզու",
        "գումար": "250000 դրամ"
    },

    {
        "հարց": "Որ երկրում է գտնվում Էյֆելյան աշտարակը",
        "տարբերակներ": [
            "Իտալիա",
            "Ֆրանսիա",
            "Գերմանիա",
            "Իսպանիա"
        ],
        "ճիշտ": "Ֆրանսիա",
        "գումար": "500000 դրամ"
    },

    {
        "հարց": "GTA V խաղի գլխավոր քաղաքը որն է",
        "տարբերակներ": [
            "Vice City",
            "Liberty City",
            "Los Santos",
            "San Fierro"
        ],
        "ճիշտ": "Los Santos",
        "գումար": "750000 դրամ"
    },

    {
        "հարց": "Արևին ամենամոտ մոլորակը որն է",
        "տարբերակներ": [
            "Վեներա",
            "Մարս",
            "Մերկուրի",
            "Յուպիտեր"
        ],
        "ճիշտ": "Մերկուրի",
        "գումար": "1000000 դրամ"
    }
]

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

main_keyboard = ReplyKeyboardMarkup(
    [["Ծրագրեր", "Խաղեր"], ["Դոնատներ", "Միլիոնատեր"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "Բարև Ընտրիր ինչի մասին խոսենք",
        reply_markup=main_keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Խաղեր":

        keyboard = [
            ["Minecraft", "CS GO"],
            ["GTA V", "It Takes Two"],
            ["PUBG Battlegrounds"],
            ["Back"]
        ]

        await update.message.reply_text(
            "Ընտրիր խաղ",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text == "Ծրագրեր":

        keyboard = [
            ["Photoshop", "VS Code"],
            ["Telegram"],
            ["Back"]
        ]

        await update.message.reply_text(
            "Ընտրիր ծրագիր",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text in խաղեր:

        context.user_data.clear()
        context.user_data["ընտրություն"] = text

        keyboard = [
            ["գին", "ինֆորմացիա"],
            ["Back"]
        ]

        await update.message.reply_text(
            f"{text} ընտրեցիր",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text in ծրագրեր:

        context.user_data.clear()
        context.user_data["ընտրություն"] = text

        keyboard = [
            ["գին", "ինֆորմացիա"],
            ["Back"]
        ]

        await update.message.reply_text(
            f"{text} ընտրեցիր",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text.lower() == "գին":

        ընտրություն = context.user_data.get("ընտրություն")

        if ընտրություն in խաղեր:
            await update.message.reply_text(
                խաղեր[ընտրություն]["գին"]
            )

        elif ընտրություն in ծրագրեր:
            await update.message.reply_text(
                ծրագրեր[ընտրություն]["գին"]
            )

        else:
            await update.message.reply_text(
                "Սկզբից ընտրիր ինչ-որ բան"
            )

    elif text.lower() == "ինֆորմացիա":

        ընտրություն = context.user_data.get("ընտրություն")

        if ընտրություն in խաղեր:
            await update.message.reply_text(
                խաղեր[ընտրություն]["ինֆորմացիա"]
            )

        elif ընտրություն in ծրագրեր:
            await update.message.reply_text(
                ծրագրեր[ընտրություն]["ինֆորմացիա"]
            )

        else:
            await update.message.reply_text(
                "Սկզբից ընտրիր ինչ-որ բան"
            )

    elif text == "Դոնատներ":

        await update.message.reply_text(
            "Դոնատների համար գրիր ադմինին @tyomkurghinyan",
            reply_markup=main_keyboard
        )

    elif text == "Միլիոնատեր":

        context.user_data.clear()
        context.user_data["հարց_index"] = 0

        հարց = հարցեր[0]

        keyboard = [
            [հարց["տարբերակներ"][0],
             հարց["տարբերակներ"][1]],

            [հարց["տարբերակներ"][2],
             հարց["տարբերակներ"][3]]
        ]

        await update.message.reply_text(
            f"{հարց['հարց']}\n\nԳումար {հարց['գումար']}",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif "հարց_index" in context.user_data:

        index = context.user_data["հարց_index"]
        հարց = հարցեր[index]

        if text == հարց["ճիշտ"]:

            հաղթած_գումար = հարց["գումար"]
            index += 1

            if index >= len(հարցեր):

                context.user_data.clear()

                await update.message.reply_text(
        
                    f"Դու հաղտեցիր միլյոնատեր խաղը շնորհավորում եմ։\n\nԴու շահեցիր {հաղթած_գումար}",
                    reply_markup=main_keyboard
                )

            else:

                context.user_data["հարց_index"] = index
                հաջորդ = հարցեր[index]

                keyboard = [
                    [հաջորդ["տարբերակներ"][0],
                     հաջորդ["տարբերակներ"][1]],

                    [հաջորդ["տարբերակներ"][2],
                     հաջորդ["տարբերակներ"][3]]
                ]

                await update.message.reply_text(
                    f"Ճիշտ պատասխան\nԴու շահեցիր {հաղթած_գումար}\n\n{հաջորդ['հարց']}\n\nԳումար {հաջորդ['գումար']}",
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard,
                        resize_keyboard=True
                    )
                )

        else:

            context.user_data.clear()

            await update.message.reply_text(
                f"Սխալ պատասխան\nՃիշտ պատասխանը {հարց['ճիշտ']} էր",
                reply_markup=main_keyboard
            )

    elif text == "Back":

        context.user_data.clear()

        await update.message.reply_text(
            "Վերադարձ գլխավոր մենյու",
            reply_markup=main_keyboard
        )

    else:

        await update.message.reply_text(
            "Չհասկացա",
            reply_markup=main_keyboard
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)

print("Bot started...")
nums = [1, 2, 3]
res = list(map(lambda x: x * 2, nums))
app.run_polling()