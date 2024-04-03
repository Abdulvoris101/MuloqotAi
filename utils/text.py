# All texts

"""Basic command texts and greetings"""

START_BOT_TEXT = """Botni boshlash uchun /start kommandasini yuboring!"""


def getGreetingsText(firstName):
    return f"""Salom! {firstName}
Men dunyodagi eng ilg'or Sun'iy intellektman

Men sizga ko'p vazifalarni hal qilishda yordam bera olaman. Masalan:
- ijtimoiy tarmoqlar uchun post, insho xabarini yozish
- kodni yozish/to'g'rilash
- rasm chizish
- uy vazifasini bajarish

Men sizga eng yangi va eng chuqur ma'lumotlarni taqdim etish bilan shug'ullanaman. Ishonch bilan xizmat qilaman 💪

🖼 Rasm chizish uchun so'rov boshiga ushbu so'zlarni qo'shishingiz kerak - generate yokida imagine

Menga o'zingiz qiziqayotgan savol yoki so'rovingizni yuboring!
"""


HELP_COMMAND = """<b>Botni qanday ishlataman?</b>
Botda  chatgptni  ishlatish uchun botga shunchaki so'rov yuborish kifoya. 
🖼 Rasm chizish uchun so'rov boshiga ushbu so'zlarni qo'shishingiz kerak - generate yokida imagine. 

<b>Bot bilan guruhda qanday yozishaman?</b>
Chatbot guruhga xabar yuborganda, bot xabari ostidagi “reply" tugmasini bosing va javobingizni kiriting yokida Xabaringizni boshida muloqotai ni nomi bilan boshlang

Misol uchun:
Muloqotai  salom, menga ....
@muloqatai salom, menga ....

<b>Botning qo'shimcha xususiyatlari</b>:
🔹<b>Avtotarjima:</b> - bilasiz chatgpt o'zbek tilini  unchalik yahshi tushunmaydi shuning uchun botda avtotarjima xususiyati mavjud, agarda avtotarjimani yoqib qo'ysangiz sizning xar bir so'rovingiz  ingliz tilga  o'tqizilib chatgptga yuboriladi va  kelgan javob esa o'zbekchaga tarjima qilinadi

Qachonki o'zbek tilida so'rov kiritsangiz avtotarjima o'zi avtomatik tarzda yonadi.

Botning rasmiy guruhi - @muloqotaigr
Botning rasmiy kanali - @muloqotai
"""


def getProfileText(
        planType,
        todaysGptRequests,
        todaysImageRequests,
        additionalGptQuota,
        additionalImageQuota
):

    availableGptRequests = "75" if planType == "Premium" else "16"
    availableImageAiRequests = "30" if planType == "Premium" else "5"

    isFree = True if planType == "Free" else False

    premiumText = """Ko’proq so’rovlar kerakmi? Unda oylik Premium obunani ulang va yanada ko’proq foydalaning!

Premium obuna bilan siz:
✅ Chatgpt turboga har kuni 75 ta so'rov;
⭐️ AI bilan har kuni 20 ta rasm generatsiya qilish;
✅ Avtotarjimon funksiyasi;
✅ Xechqanday reklama yo'q;
✅ So’rovlar orasida pauza yo’q;
✅ Xabarlarni cheksiz tarjima qilish.
✅ Javoblar kreativroq.

Premium obunani ulash uchun /premium bo’limiga o’ting."""


    return f"""⚡️ Obuna turi: {planType}
🤖 GPT modeli: gpt-3.5-turbo

Limitlar: 
• GPT-3.5 bugungi so’rovlar: {todaysGptRequests}/{availableGptRequests}
• Rasm generatsiya: {todaysImageRequests}/{availableImageAiRequests}
• Qo'shimcha GPT-3.5 so'rovlar: {additionalGptQuota}
• Qo'shimcha rasm so'rovlari: {additionalImageQuota}

{premiumText if isFree else ''}
"""


""" Premium and plan texts """


def subscriptionInvoiceText(price):
    return f"""1/2
To'lov tafsilotlari:

<b>Mahsulot:</b> Premium obuna
<b>1 oylik obuna narxi:</b> {price} so'm
<b>Umumiy summa:</b> <b>{price} so'm</b>

Xaridni yakunlash uchun <b>{price}</b> so'm miqdorini quyidagi kartaga oʻtkazing:

<b>Karta raqami:</b> <code>5614 6814 0539 6510</code>
<b>Karta egasi</b>: TULKIN XUDAYBERGANOV

⚠️ Ushbu kartaga to'lov qilganingizdan so'ng bizga to'lov skrinshotini yuboring
Biz sizning to'lovingizni qo'lda tekshirib chiqamiz va sizga obuna taqdim etamiz.

Toʻlov jarayonida biror muammoga duch kelsangiz yoki savollaringiz boʻlsa, bizga murojat qiling - @texnosupportuzbot | @abdulvoris_101
"""


PAYMENT_STEP_1 = """2/2
To'lovni tasdiqlash uchun bizga to'lov skrinshotini yuboring 👇
"""

PAYMENT_STEP_2 = """
Ajoyib! Sizning to'lovingiz yaqin soatlar ichida tekshirilib chiqib, 
sizga premium obuna taqdim etiladi. 
Yaqin soatlar ichida sizga premium obuna bo'yicha xabar keladi.
Bizni tanlaganiz uchun rahmat 🫡

Agarda biror savolingiz bo'lsa, bizga murojat qiling - @texnosupportuzbot | @abdulvoris_101
"""

# Plans text

PLAN_DESCRIPTION_TEXT = """
Xozirgi obuna quyidagilarni o'z ichiga oladi:
✅ Chatgptga har kuni 16 ta so'rov;
⭐️ AI bilan 5 ta rasm generatsiya qilish;
✅ Avtotarjimon funksiyasi;
✅ 5ta xabarni tarjima qilish.


Ko'proq kerakmi? 25.000 so'm evaziga bir oylik premium tarifga obuna bo'ling.

Premium obuna bilan siz:
✅ Chatgpt turboga har kuni 75 ta so'rov;
⭐️ AI bilan har kuni 20 ta rasm generatsiya qilish;
✅ Avtotarjimon funksiyasi;
✅ Xechqanday reklama yo'q;
✅ So’rovlar orasida pauza yo’q;
✅ Xabarlarni cheksiz tarjima qilish.
✅ Javoblar kreativroq.
"""

""" Limits """


def getLimitReached(isPremium):
    usedRequests = 75 if isPremium else 16
    freeText = """ruxsat etilgan maksimal bepul foydalanishga erishdingiz. ChatGPT-ni abadiy bepul taqdim etish biz uchun qimmat.
Yanada ko'proq so'rov uchun premium tarifga obuna bo'ling. /premium""" if not isPremium else ""
    return f"""Afsuski sizning kunlik limitingiz tugadi, {freeText}
{usedRequests}/{usedRequests}
"""


LIMIT_GROUP_REACHED = """Afsuski guruhning kunlik limiti tugadi. 
So'rovlarni ko'paytirish uchun bizga donat qilib yordam berishingiz mumkin

Har qanday to'lov o'tgandan so'ng biz zudlik bilan guruh uchun qo'shimcha chatgpt va rasm generatsiya so'rovlarini sotib olib sizlarga taqdim etamiz

150/150
/donate"""

DONATE = f"""
🌟 Bizga donat qilayotganiz uchun katta rahmat! 
Sizning donatingiz juda qadrlanadi va mazmunli o'zgarishlarga olib keladi.

Donat uchun karta informatsiyasi:

<b>Karta raqami:</b> <code>5614 6814 0539 6510</code>
<b>Karta egasi</b>: TULKIN XUDAYBERGANOV

Savol va takliflar uchun - @texnosupportuzbot
"""

PREMIUM_GRANTED_TEXT = """Tabriklaymiz sizga premium obuna taqdim etildi. Bizni tanlaganiz uchun rahmat 😊🎉"""
SUBSCRIPTION_END = """🚀 Obunani yangilash vaqti keldi!

Salom Qadrli Foydalanuvchi 👋,

Obunangiz muddati tugadi! Premium imtiyozlardan foydalanishda davom etish uchun “/premium” kommandasini kiriting.

Bizni tanlaganiz uchun tashakkur 🌟
"""


def getStatisticsText(
        usersCount,
        activeUsers,
        activeUsersOfDay,
        usersUsedOneDay,
        usersUsedOneWeek,
        usersUsedOneMonth,
        premiumUsers,
        limitReachedUsers,
        allMessages,
        avgUsersMessagesCount,
        todayMessages,
        lastUpdate,
        latestUser
):
    return f"""👤 Foydalanuvchilar - {usersCount}
💥 Aktiv Foydalanuvchilar - {activeUsers}
✨  Bugungi Aktiv Foydalanuvchilar - {activeUsersOfDay}
1️⃣  Kun ishlatgan foydalanuvchilar - {usersUsedOneDay}
📆 1 hafta ishlatgan Foydalanuvchilar - {usersUsedOneWeek}
🗓  1 oy ishlatgan Foydalanuvchilar - {usersUsedOneMonth}
🎁 Premium Foydalanuvchilar - {premiumUsers}
🛑 Bugungi limiti tugagan Foydalanuvchilar - {limitReachedUsers}
📨 Xabarlar - {allMessages}
📩 User uchun o'rtacha xabar - {avgUsersMessagesCount}
✉️ Bugungi xabarlar - {todayMessages}

Eng oxirgi aktivlik - {lastUpdate}
Eng oxirgi aktivlik ko'rstgan user - {latestUser}"""


def getRejectReason(reason):
    return f"""Afsuski sizning premium obunaga bo'lgan so'rovingiz bekor qilindi.
Sababi: {reason}
Biror xatolik ketgan bo'lsa bizga murojat qiling: @texnosupportuzbot
"""


INLINE_BUTTONS_GUIDE = """Inline buttonlarni kiriting. 
Misol uchun\n`./Test-t.me//texnomasters\n./Test2-t.me//texnomasters`"""

# Ai chat handler

FEEDBACK_MESSAGE = """Bot bilan bo'lgan tajribangizni yozib qoldiring, bu bilan siz botni rivoji uchun xissa qo'shgan bo'lasiz! 
Sizning fikr-mulohazalaringiz xizmatimizni yaxshilashga yordam beradi. Biz sizning har bir fikringizni qadrlaymiz! ✨"""

FEEDBACK_GUIDE_MESSAGE = """Ushbu savollarga javob berib bizga yordam bering
1. Bot siz uchun qanchalik foydali 0-10 gacha baxolang
2. Botda yana qanday jihatlarni ko'rishni xoxlar edingiz? 
3. Bot bilan suxbatlashayotganda sizda qandaydir xatolik ro'y berdimi? Bo'lgan bo'lsa qanday xatolik?
4. Botni qayerdan eshitib kirdingiz?

Ushbu savollarga qisqagina javob yo'llab bizga yordam bering 😊
"""

PROCESSING_MESSAGE = "⏳"
ENTER_AGAIN = "Iltimos boshqatan so'rov yuboring"
TOKEN_REACHED = "Savolni qisqartiribroq yozing"


def getNewChatMember(firstName):
    return f"""👋 Assalomu alaykum! {firstName}, 
Sizni yana bir bor ko'rib turganimdan xursandman. Bugun sizga qanday yordam bera olaman? 
Men bilan qiziqarli suxbat qurishga tayyormisiz?"
"""


NOT_SUBSCRIBED = "Bu xizmatdan foydalanish uchun premiumga obuna bo'lishingiz kerak. /premium buyrug'i yordamida obuna bo'ling"
LIMIT_TRANSLATION_REACHED = "Afsuski sizning tarjima uchun limitingiz tugadi. Cheksiz tarjima uchun premiumga obuna bo'lishingiz kerak /premium "
# ERRORS

NOT_AVAILABLE_GROUP = """Bu guruhda rasm generatsiya qilib bo'lmaydi!"""
IMAGE_GEN_NOT_AVAILABLE = """Bu guruhda rasm generatsiya qilib bo'lmaydi!"""
IMAGE_GEN_ERROR = """Rasm generatsiyasi jarayonida xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring."""

