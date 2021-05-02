from bs4 import BeautifulSoup as bs
import requests as req
import tkinter as tk
from Vaccines_daily_window import WindowApplication


def main():
	r = req.get('https://www.medonet.pl/koronawirus/to-musisz-wiedziec,zasieg-koronawirusa-covid-19--mapa-,artykul,54726942.html?utm_source=sgonet&utm_medium=referral&utm_campaign=mapasgonet&srcc=mapasgonet')

	soup = bs(r.content, "html.parser")

	li_part = soup.find_all("li", attrs = {"class":"item"})

	category_names = ['Liczba zakażeń', 'Liczba ozdrowieńców', 'Liczba zgonów']
	category_names_iter = iter(category_names)


	info_dict = dict()
	key_words = ['Ogółem', 'Pierwsza dawka', 'W pełni zaszczepieni', 'Ostatnia doba']

	for part in li_part:
		span_item = part.find("span", attrs={"class":"value"}) 
		if not span_item is None:
			if span_item.text.split(": ")[0] in key_words and span_item.text.split(": ")[0] not in info_dict.keys():
				info_dict[span_item.text.split(": ")[0]] = int(span_item.text.split(": ")[1].replace("\xa0", "").replace(" ",""))
			elif span_item.text.split(": ")[0] == 'Polska':
				info_dict[next(category_names_iter)] = int(span_item.text.split(": ")[1].replace("\xa0", "").replace(" ","").split("(")[0])
			else:
				pass

	del info_dict['Liczba zakażeń']
	del info_dict['Liczba zgonów']


	Population = 37_815_000


	info_dict_pct = {key + " w %": round((val/Population)*100, 4) for key, val in info_dict.items()}
	

	text_to_be_displayed = "\nOgólne dane:\n"

	for ky, val in info_dict.items():
		text_to_be_displayed += f"{ky}: {val:,}\n"
	
	text_to_be_displayed += f"Estymat x5: {info_dict['Liczba ozdrowieńców'] * 5:,}\n"
	text_to_be_displayed += f"Estymat x6: {info_dict['Liczba ozdrowieńców'] * 6:,}\n"

	text_to_be_displayed += "\n\nDane w procentach:\n"
	
	for ky, val in info_dict_pct.items():
		text_to_be_displayed += f"{ky}: {val}\n"

	text_to_be_displayed += f"Estymat x5 w %: {info_dict_pct['Liczba ozdrowieńców w %'] * 5}\n"
	text_to_be_displayed += f"Estymat x6 w %: {info_dict_pct['Liczba ozdrowieńców w %'] * 6}\n"
	
	window = tk.Tk()
	window_app = WindowApplication(master=window)
	window_app.display_text(text_to_be_displayed)
	tk.mainloop()



if __name__ == "__main__":
	main()