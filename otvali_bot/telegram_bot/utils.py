
from models.client import get_client_by_tg_id
from .mytelebot import myTeleBot
import time

botForUtil = None
def init_util_bot(bot: myTeleBot):
    global botForUtil
    botForUtil = bot

  
def admin_only(func):
    def wrapper(message):
        client = get_client_by_tg_id(message.from_user.id)
        if client is None or (not client.is_admin):
            botForUtil.send_message(message.chat.id, "You can't do it!")
            return
        return func(message)
    return wrapper

def approved_only(func):
    def wrapper(message):
        client = get_client_by_tg_id(message.from_user.id)
        if client is None or (not client.is_approved):
            botForUtil.send_message(message.chat.id, "Your account haven't been approved! You can't do it")
            return
        return func(message)
    return wrapper
    


def delete_message_after_a_minute(bot, chat_id, message_id, duration):
    time.sleep(60)
    bot.delete_message(chat_id, message_id)


def is_convertible_to_int(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False
    

def get_country_emoji(country_name):
    return country_emojis.get(country_name, '🌍')


country_emojis = {
    "Andorra": "🇦🇩",
    "United Arab Emirates": "🇦🇪",
    "Afghanistan": "🇦🇫",
    "Antigua and Barbuda": "🇦🇬",
    "Anguilla": "🇦🇮",
    "Albania": "🇦🇱",
    "Armenia": "🇦🇲",
    "Angola": "🇦🇴",
    "Antarctica": "🇦🇶",
    "Argentina": "🇦🇷",
    "American Samoa": "🇦🇸",
    "Austria": "🇦🇹",
    "Australia": "🇦🇺",
    "Aruba": "🇦🇼",
    "Åland Islands": "🇦🇽",
    "Azerbaijan": "🇦🇿",
    "Bosnia and Herzegovina": "🇧🇦",
    "Barbados": "🇧🇧",
    "Bangladesh": "🇧🇩",
    "Belgium": "🇧🇪",
    "Burkina Faso": "🇧🇫",
    "Bulgaria": "🇧🇬",
    "Bahrain": "🇧🇭",
    "Burundi": "🇧🇮",
    "Benin": "🇧🇯",
    "Saint Barthélemy": "🇧🇱",
    "Bermuda": "🇧🇲",
    "Brunei Darussalam": "🇧🇳",
    "Bolivia": "🇧🇴",
    "Bonaire, Sint Eustatius and Saba": "🇧🇶",
    "Brazil": "🇧🇷",
    "Bahamas": "🇧🇸",
    "Bhutan": "🇧🇹",
    "Bouvet Island": "🇧🇻",
    "Botswana": "🇧🇼",
    "Belarus": "🇧🇾",
    "Belize": "🇧🇿",
    "Canada": "🇨🇦",
    "Cocos (Keeling) Islands": "🇨🇨",
    "Congo": "🇨🇩",
    "Central African Republic": "🇨🇫",
    "Congo": "🇨🇬",
    "Switzerland": "🇨🇭",
    "Côte D'Ivoire": "🇨🇮",
    "Cook Islands": "🇨🇰",
    "Chile": "🇨🇱",
    "Cameroon": "🇨🇲",
    "China": "🇨🇳",
    "Colombia": "🇨🇴",
    "Costa Rica": "🇨🇷",
    "Cuba": "🇨🇺",
    "Cape Verde": "🇨🇻",
    "Curaçao": "🇨🇼",
    "Christmas Island": "🇨🇽",
    "Cyprus": "🇨🇾",
    "Czech Republic": "🇨🇿",
    "Germany": "🇩🇪",
    "Djibouti": "🇩🇯",
    "Denmark": "🇩🇰",
    "Dominica": "🇩🇲",
    "Dominican Republic": "🇩🇴",
    "Algeria": "🇩🇿",
    "Ecuador": "🇪🇨",
    "Estonia": "🇪🇪",
    "Egypt": "🇪🇬",
    "Western Sahara": "🇪🇭",
    "Eritrea": "🇪🇷",
    "Spain": "🇪🇸",
    "Ethiopia": "🇪🇹",
    "Finland": "🇫🇮",
    "Fiji": "🇫🇯",
    "Falkland Islands (Malvinas)": "🇫🇰",
    "Micronesia": "🇫🇲",
    "Faroe Islands": "🇫🇴",
    "France": "🇫🇷",
    "Gabon": "🇬🇦",
    "United Kingdom": "🇬🇧",
    "Grenada": "🇬🇩",
    "Georgia": "🇬🇪",
    "French Guiana": "🇬🇫",
    "Guernsey": "🇬🇬",
    "Ghana": "🇬🇭",
    "Gibraltar": "🇬🇮",
    "Greenland": "🇬🇱",
    "Gambia": "🇬🇲",
    "Guinea": "🇬🇳",
    "Guadeloupe": "🇬🇵",
    "Equatorial Guinea": "🇬🇶",
    "Greece": "🇬🇷",
    "South Georgia": "🇬🇸",
    "Guatemala": "🇬🇹",
    "Guam": "🇬🇺",
    "Guinea-Bissau": "🇬🇼",
    "Guyana": "🇬🇾",
    "Hong Kong": "🇭🇰",
    "Heard Island and Mcdonald Islands": "🇭🇲",
    "Honduras": "🇭🇳",
    "Croatia": "🇭🇷",
    "Haiti": "🇭🇹",
    "Hungary": "🇭🇺",
    "Indonesia": "🇮🇩",
    "Ireland": "🇮🇪",
    "Israel": "🇮🇱",
    "Isle of Man": "🇮🇲",
    "India": "🇮🇳",
    "British Indian Ocean Territory": "🇮🇴",
    "Iraq": "🇮🇶",
    "Iran": "🇮🇷",
    "Iceland": "🇮🇸",
    "Italy": "🇮🇹",
    "Jersey": "🇯🇪",
    "Jamaica": "🇯🇲",
    "Jordan": "🇯🇴",
    "Japan": "🇯🇵",
    "Kenya": "🇰🇪",
    "Kyrgyzstan": "🇰🇬",
    "Cambodia": "🇰🇭",
    "Kiribati": "🇰🇮",
    "Comoros": "🇰🇲",
    "Saint Kitts and Nevis": "🇰🇳",
    "North Korea": "🇰🇵",
    "South Korea": "🇰🇷",
    "Kuwait": "🇰🇼",
    "Cayman Islands": "🇰🇾",
    "Kazakhstan": "🇰🇿",
    "Lao People's Democratic Republic": "🇱🇦",
    "Lebanon": "🇱🇧",
    "Saint Lucia": "🇱🇨",
    "Liechtenstein": "🇱🇮",
    "Sri Lanka": "🇱🇰",
    "Liberia": "🇱🇷",
    "Lesotho": "🇱🇸",
    "Lithuania": "🇱🇹",
    "Luxembourg": "🇱🇺",
    "Latvia": "🇱🇻",
    "Libya": "🇱🇾",
    "Morocco": "🇲🇦",
    "Monaco": "🇲🇨",
    "Moldova": "🇲🇩",
    "Montenegro": "🇲🇪",
    "Saint Martin (French Part)": "🇲🇫",
    "Madagascar": "🇲🇬",
    "Marshall Islands": "🇲🇭",
    "Macedonia": "🇲🇰",
    "Mali": "🇲🇱",
    "Myanmar": "🇲🇲",
    "Mongolia": "🇲🇳",
    "Macao": "🇲🇴",
    "Northern Mariana Islands": "🇲🇵",
    "Martinique": "🇲🇶",
    "Mauritania": "🇲🇷",
    "Montserrat": "🇲🇸",
    "Malta": "🇲🇹",
    "Mauritius": "🇲🇺",
    "Maldives": "🇲🇻",
    "Malawi": "🇲🇼",
    "Mexico": "🇲🇽",
    "Malaysia": "🇲🇾",
    "Mozambique": "🇲🇿",
    "Namibia": "🇳🇦",
    "New Caledonia": "🇳🇨",
    "Niger": "🇳🇪",
    "Norfolk Island": "🇳🇫",
    "Nigeria": "🇳🇬",
    "Nicaragua": "🇳🇮",
    "Netherlands": "🇳🇱",
    "Norway": "🇳🇴",
    "Nepal": "🇳🇵",
    "Nauru": "🇳🇷",
    "Niue": "🇳🇺",
    "New Zealand": "🇳🇿",
    "Oman": "🇴🇲",
    "Panama": "🇵🇦",
    "Peru": "🇵🇪",
    "French Polynesia": "🇵🇫",
    "Papua New Guinea": "🇵🇬",
    "Philippines": "🇵🇭",
    "Pakistan": "🇵🇰",
    "Poland": "🇵🇱",
    "Saint Pierre and Miquelon": "🇵🇲",
    "Pitcairn": "🇵🇳",
    "Puerto Rico": "🇵🇷",
    "Palestinian Territory": "🇵🇸",
    "Portugal": "🇵🇹",
    "Palau": "🇵🇼",
    "Paraguay": "🇵🇾",
    "Qatar": "🇶🇦",
    "Réunion": "🇷🇪",
    "Romania": "🇷🇴",
    "Serbia": "🇷🇸",
    "Russia": "🇷🇺",
    "Rwanda": "🇷🇼",
    "Saudi Arabia": "🇸🇦",
    "Solomon Islands": "🇸🇧",
    "Seychelles": "🇸🇨",
    "Sudan": "🇸🇩",
    "Sweden": "🇸🇪",
    "Singapore": "🇸🇬",
    "Saint Helena, Ascension and Tristan Da Cunha": "🇸🇭",
    "Slovenia": "🇸🇮",
    "Svalbard and Jan Mayen": "🇸🇯",
    "Slovakia": "🇸🇰",
    "Sierra Leone": "🇸🇱",
    "San Marino": "🇸🇲",
    "Senegal": "🇸🇳",
    "Somalia": "🇸🇴",
    "Suriname": "🇸🇷",
    "South Sudan": "🇸🇸",
    "Sao Tome and Principe": "🇸🇹",
    "El Salvador": "🇸🇻",
    "Sint Maarten (Dutch Part)": "🇸🇽",
    "Syrian Arab Republic": "🇸🇾",
    "Swaziland": "🇸🇿",
    "Turks and Caicos Islands": "🇹🇨",
    "Chad": "🇹🇩",
    "French Southern Territories": "🇹🇫",
    "Togo": "🇹🇬",
    "Thailand": "🇹🇭",
    "Tajikistan": "🇹🇯",
    "Tokelau": "🇹🇰",
    "Timor-Leste": "🇹🇱",
    "Turkmenistan": "🇹🇲",
    "Tunisia": "🇹🇳",
    "Tonga": "🇹🇴",
    "Turkey": "🇹🇷",
    "Trinidad and Tobago": "🇹🇹",
    "Tuvalu": "🇹🇻",
    "Taiwan": "🇹🇼",
    "Tanzania": "🇹🇿",
    "Ukraine": "🇺🇦",
    "Uganda": "🇺🇬",
    "United States Minor Outlying Islands": "🇺🇲",
    "United States": "🇺🇸",
    "Uruguay": "🇺🇾",
    "Uzbekistan": "🇺🇿",
    "Vatican City": "🇻🇦",
    "Saint Vincent and The Grenadines": "🇻🇨",
    "Venezuela": "🇻🇪",
    "Virgin Islands, British": "🇻🇬",
    "Virgin Islands, U.S.": "🇻🇮",
    "Viet Nam": "🇻🇳",
    "Vanuatu": "🇻🇺",
    "Wallis and Futuna": "🇼🇫",
    "Samoa": "🇼🇸",
    "Yemen": "🇾🇪",
    "Mayotte": "🇾🇹",
    "South Africa": "🇿🇦",
    "Zambia": "🇿🇲",
    "Zimbabwe": "🇿🇼"
}
