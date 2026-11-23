# Kerättävät esineet
class Item:
    def __init__(self, name, foundText, usedText, itemNotUsed, isSingleUse, usedIn):
        self.name = name # esineen nimi
        self.foundText = foundText # tämä tulostuu esineen löytyessä
        self.usedText = usedText # tämä tulostuu kun esinettä käytetään
        self.itemNotUsed = itemNotUsed # tämä tulostuu kun esinettä ei voi käyttää
        self.isSingleUse = isSingleUse # onko esine kertakäyttöinen
        self.usedIn = usedIn # missä sijainnissa esine on käytetty

    # Muokkaa esineen sanakirjamuotoon
    def to_dictionary(self):
        return {
            "name": self.name,
            "foundText": self.foundText,
            "usedText": self.usedText,
            "itemNotUsed": self.itemNotUsed,
            "isSingleUse": self.isSingleUse,
            "usedIn": [location.name for location in self.usedIn] if self.usedIn else []
        }


# kartta = Item(
#     name = "Kartta",
#     foundText = "Löysit kartan. Tästä voi olla paljon hyötyä.",
#     usedText = "  ╭───────────────═══════════════════───────═════╗\n"
#                "  │                                              ║\n"
#                "  │           皿  ⌂ ⌂             ₅        ^     ║\n"
#                "  ║    ╭╌╌ [ Keskusta ] ══╤═ [ Koti ]      N     ║\n"
#                "  ║    ┆      ⁹ ║ ⌂⌂      │      ┆              ─╢\n"
#                "  │ [ Kuja ]  ⌂ ╚═╗       ╰─ [ Metsä ] ╌╌╌╮      │\n"
#                "  │    ┆ ¹        ║          ♣Ψ  │ ⌂      ┆ ₄    │\n"
#                "  ║    ┆      [ Kauppa ]       ♣ │    [ Raunio ] ║\n"
#                "  ╠═   ┆           ²             │ Ψ      ┆      ║\n"
#                "  ║    ╰╌ [ ??? ] † †        [ Pelto ] ╌╌╌╯      ║\n"
#                "  ║                †      ▲▲      ⁷      ~~~     │\n"
#                "  ║                                              │\n"
#                "  ╚═════════─────════════────────────────────────╯\n"
#     )

kärryt = Item(
    name = "Kärryt",
    foundText = "Löysit kottikärryt. Niillä saat kannettua raskaat tavarat paikasta toiseen.",
    usedText = "Tätä esinettä ei voi käyttää, ainoastaan tutkia.",
    itemNotUsed = "Näihin kottikärryihin mahtuu yllättävän paljon tavaraa. Nyt saat kuljetettua myös raskaita esineitä.",
    isSingleUse = True,
    usedIn = []
    )

työkalut = Item(
    name = "Työkalut",
    foundText = "Löysit sattumalta myös ikivanhan työkalulaatikkosi. Nappaat mukaasi sahan, vasaran, poran, sekä ruuvimeisselin. Nyt on aika palata takaisin kauppaan.",
    usedText = "Tätä esinettä ei voi käyttää, ainoastaan tutkia.",
    itemNotUsed = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen.",
    isSingleUse = True,
    usedIn = []
    )

# Funktionaaliset esineet
rakennuslupa = Item(
    name = "Rakennuslupa",
    foundText = "Otat mukaan rakennusluvan. Voit nyt lähteä seikkailemaan ympäri kaupunkia. Valitse rakennuspaikka käyttämällä rakennuslupa inventaariostasi.",
    usedText = "Pääset vihdoin aloittamaan rakennusprojektisi. Sinulta puuttuu kuitenkin vielä työkalut sekä rakennusmateriaalit.",
    itemNotUsed = "Et voi rakentaa tähän. Keskustasta ja pellolta pitäisi löytyä rakennusalueita.",
    isSingleUse = True,
    usedIn = []
    )

kirjat = Item(
    name = "Kirjat",
    foundText = "Tila on täynnä erilaisia oppikirjoja. Mitä koulu olisikaan ilman oppimateriaaleja? Päätät ottaa ison kasan kirjoja mukaan.",
    usedText = "Laitat kirjat koulun varastotilaan odottamaan koulun avauspäivää.",
    itemNotUsed = "Kirjakokoelmastasi löytyy mm. historiaa, matikkaa, äidinkieltä ja luonnontieteitä. Ne kannattaa viedä koululle heti kun olet saanut sen rakennettua.",
    isSingleUse = True,
    usedIn = []
    )

sorkkarauta = Item(
    name = "Sorkkarauta",
    foundText = "Paniikki meinaa iskeä, kunnes havaitset huoneen nurkassa olevan sorkkaraudan. Ehkä saat oven tiirikoitua auki.",
    usedText = "Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle.",
    itemNotUsed = "Et ole nyt väkivaltaisella tuulella.",
    isSingleUse = False,
    usedIn = []
    )

avain = Item(
    name = "Avain",
    foundText = "Ojennat sorkkaraudan lipaston alle ja nykäiset vajan avaimen kätesi ulottuville.",
    usedText = "Vajan lukko aukeaa ja näet sisällä kaikenlaista siistiä.",
    itemNotUsed = "Avain ei käy tähän.",
    isSingleUse = True,
    usedIn = []
    )

harava = Item(
    name = "Harava",
    foundText = "Vajan seinustalla nojaa myös harava. Toivottavasti se nyt kestää raskaampiakin töitä.",
    usedText = "Haravoit pellolta lehtiä, heinää ja muuta roskaa. Jossain kohtaa haravasi kuitenkin hajoaa.",
    itemNotUsed = "Vaikka kuinka tahtoisit pitää kaupunkia siistinä, sinulla ei ole nyt aikaa siihen.",
    isSingleUse = True,
    usedIn = []
    )

rahaa = Item(
    name = "Rahaa",
    foundText = "Löysit possupankkisi, jonka tungit aikoinaan täyteen seteleitä. Juuri sopivasti rahaa rakennusmateriaalien ostamiseen.",
    usedText = "Et ole säästänyt turhaan kaikkien näiden vuosien ajan. Kaikki rahasi kuluu rakennusmateriaaleihin ja nyt toivot ettei lisäkustannuksia tule enempää.",
    itemNotUsed = "Sinulla ei ole mitään ostettavaa.",
    isSingleUse = True,
    usedIn = []
    )

materiaalit = Item(
    name = "Materiaalit",
    foundText = "Hankit myös kasan lautaa, ruuveja, nauloja, peltiä ja kaikkea muuta tarvittavaa.",
    usedText = "Nyt kun vihdoin löysit kaiken tarvitsemasi, sait rakennettua pienen koulun. Budjettisi ei ollut kovin suuri, joten tiloja on rajallisesti. Voit nyt halutessasi palata kotiin nukkumaan tai jatkaa tutkimista. Koulu avataan vasta huomenna.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    usedIn = []
    )

romua = Item(
    name = "Romua",
    foundText = "Löysit ison kasan romua, jota voit käyttää rakennusmateriaalina. Näillä saat laajennettua koulun tiloja huomattavasti.",
    usedText = "Laajensit koulua rakentamalla uusia luokkahuoneita sekä varastotilan.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    usedIn = []
    )

yöpuku = Item(
    name = "Yöpuku",
    foundText = "Nappaat kaapista sinisen yöpukusi. Näytät ihan Herra Hakkaraiselta se päällä. Vaihda vaatteet ennen nukkumaanmenoa.",
    usedText = "Pitkästä aikaa pääsee taas nukkumaan. Koulu avataankin jo huomenna ja odotat innolla seuraavaa päivää.",
    itemNotUsed = "Älä nyt hyvä ihminen rupea täällä vaihtamaan vaatteita!!",
    isSingleUse = False,
    usedIn = []
    )

allItems = [kärryt, kirjat, työkalut, rakennuslupa, sorkkarauta, avain, harava, rahaa, materiaalit, romua, yöpuku]