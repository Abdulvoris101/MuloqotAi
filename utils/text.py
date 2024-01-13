# core

from utils import constants

COST = constants.AQSHA_COST

START_COMMAND = """🤖 Salom! Men MuloqotAi, sizning shaxsiy 
yordamchingizman.
Avtotarjimon yoniq xolatda.
Batafsil ma'lumot uchun - /help
"""

HOW_TO_HELP_TEXT = """Sizga qanday yordam bera olaman?"""

HELP_COMMAND = """<b>Botni qanday ishlataman?</b>
Botda  chatgptni  ishlatish uchun botga shunchaki so'rov yuborish kifoya. 
Rasm generatsiyasi uchun esa shu komandani yuboring: /art prompt. Prompt o'rniga o'zingizni so'rovingizni yuboring. 

<b>Botning qo'shimcha xususiyatlari</b>:
🔹<b>Avtotarjima:</b> - bilasiz chatgpt o'zbek tilini tushunmaydi shuning uchun botda avtotarjima xususiyati mavjud, agarda avtotarjimani yoqib qo'ysangiz sizning xar bir so'rovingiz tarjimon orqali ingliz tilga  o'tqizilib chatgptga yuboriladi va  kelgan javob esa o'zbekchaga tarjima qilinadi. Bu bilan siz ingliz tilini bilmasdan turib chatgptni to'liqona ishlatishingiz mumkin bo'ladi.

"""


GROUP_INFO_COMMAND = """Shaxsiy va guruh suhbatlaringizda yordam beradigan foydali yordamchi! Ushbu botning <b>guruhda</b> ishlash tartibi quyidagicha:

1️⃣ <b>Guruhga qo'shish</b>: MuloqotAIdan foydalanish uchun, uningni Telegram gruhingizga qo'shing. Bu uchun "@muloqataibot" ni qidiring va uningni gruhga taklif qiling.

2️⃣ <b>Admin huquqlarini berish</b>: MuloqotAItning samarali ishlashi uchun uningni admin sifatida qo'shish kerak. Uningga to'g'ri admin huquqlarini berishni unutmang, masalan, xabarlarni o'chirish (ixtiyoriy) va boshqa sozlamalarni boshqarish.

3️⃣ <b>Gruhda suhbatlashish</b>: Bot bilan suhbat qurish uchun unga reply tarzida so'rov yuboring. Guruh a'zolari savollarni so'rash, ma'lumot so'ralish, yordam so'ralish yoki qiziqarli suhbatlar olib borishlari mumkin.

➕ <b>Ochiq guruh:</b> @muloqataigr"""


ABILITY_COMMAND = """💡 Aqlli: Ko'plab mavzularni tushunish va javob berishga tayyorman. Umumiy bilimdan ma'lumotlarni qidirishga qadar, 
sizga aniqligi va maqbul javoblarni taklif etishim mumkin.

🧠 Dono: Men doimiy o'rganish va rivojlanishda, yangi ma'lumotlarga va foydalanuvchi bilan bo'lishuvlarga moslashishim mumkin. Aqlli muloqotlarni taklif etishim mumkin.

🌄 Rassom: Mening yana bir qobilyatlarimdan biri bu rasm generatsiya qila olishim. Men sizga xar qanday turdagi ajoyib rasmlarni generatsiya qilib olib bera olaman

⚙️ Avtotarjimon: Meni siz bilan o'zbek tilida yanada yahshiroq muloqot qila olishim uchun, avtotarjima funksiyasini ishlataman. Endi siz ingliz tilida qiynalib menga yozishingiz shart emas. Bu funksiya ixtiyoriy xoxlagan paytiz o'chirib qo'yishingiz mumkin."""


NEW_MEMBER_TEXT = """👋 Assalomu alaykum! Mening ismim MuloqotAI 
Men sizga yordam berish uchun yaratilgan aqlli chatbotman. 
Bot ishlashi uchun menga administrator huquqlarini bering
😊 Ko'proq foydam tegishi uchun /help kommandasini yuborib men bilan yaqinroq tanishib chiqing
"""

GREETINGS_TEXT = "Assalomu aleykum Men Muloqot AI man sizga qanday yordam bera olaman?"


def buy_text(price):
        
    BUY_TEXT = f"""
To'lov tafsilotlari:

<b>Mahsulot:</b> Premium obuna
<b>1 haftalik obuna narxi:</b> {price} so'm
<b>Umumiy summa:</b> <b>{price} so'm</b>

Xaridni yakunlash uchun <b>{price}</b> so'm miqdorini quyidagi kartaga oʻtkazing:

<b>Karta raqami:</b> <code>5614 6814 0539 6512</code>
<b>Karta egasi</b>: TULKIN XUDAYBERGANOV

To'lov o'tgandan so'ng to'lovingiz qo'lda tekshirilib chiqiladi va sizga obuna taqdim etiladi.

Toʻlov jarayonida biror muammoga duch kelsangiz yoki savollaringiz boʻlsa, bizga murojat qiling - @texnosupportuzbot | @abdulvoris_101
"""
    return BUY_TEXT

PAYMENT_STEP1 = """
Biz xozir sizning to'lovingizni o'zimiz qo'lda tekshirib chiqamiz,
uning uchun esa bizga yuborgan kartangizdagi ismingizni yozing 👇
"""

PAYMENT_STEP2 = """
Ajoyib! Sizning to'lovingiz yaqin soatlar ichida tekshirilib chiqib, 
sizga premium obuna taqdim etiladi. 
Yaqin soatlar ichida sizga premium obuna bo'yicha xabar keladi.
Bizni tanlaganiz uchun rahmat 🫡

Agarda biror savolingiz bo'lsa, bizga murojat qiling - @texnosupportuzbot | @abdulvoris_101
"""

# Plans

PLAN_TEXT = """
Xozirgi obuna quyidagilarni o'z ichiga oladi:
✅ Chatgptga har kuni 20 ta so'rov;
⭐️ AI bilan 5 ta rasm generatsiya qilish;
✅ Avtotarjimon funksiyasi;
✅ Birinchi 10ta so'rov uchun vaqt chegarasi yo'q;
⚠️ Keyingi so’rovlarda vaqt chegarasi mavjud;

Ko'proq kerakmi? 6000 so'm evaziga bir haftalik premium tarifga obuna bo'ling.

Premium obuna bilan siz:
✅ Chatgptga turboga har kuni 100 ta so'rov;
⭐️ AI bilan 20 ta rasm generatsiya qilish;
✅ Avtotarjimon funksiyasi;
✅ Xechqanday reklama yo'q;
✅ So’rovlar orasida pauza yo’q;
✅ Javoblar kreativroq.
"""

LIMIT_REACHED = """Afsuski sizning kunlik limitingiz tugadi. 
Yanada ko'proq so'rov uchun premium tarifga obuna bo'ling
/premium"""

PREMIUM_GAVE = """Tabriklaymiz sizga premium obuna taqdim etildi. Bizni tanlaganiz uchun rahmat 😊🎉"""

SUBSCRIPTION_END = """🚀 Obunani yangilash vaqti keldi!

Salom Qadrli Foydalanuvchi 👋,

Obunangiz muddati tugadi! Premium imtiyozlardan foydalanishda davom etish uchun “/premium” kommandasini kiriting.

Bizni tanlaganiz uchun tashakkur 🌟
"""
     
    