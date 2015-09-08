from bs4 import BeautifulSoup

def quick_test():
    content = open("test_site/tt2.asp", "r").read()
    soup = BeautifulSoup(content, "lxml")
    for elem in soup.find_all("tr"):
        if elem.findChild("p") != None:
            for child in elem.find_all("td"):
                text = child.text.replace(" ", "").split()
		for part in text:
		    print part
                break
        else:
            continue
        break

if __name__ == "__main__":
    quick_test()
