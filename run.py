from kapwrapper import Wrapper

if __name__ == '__main__':
    kap_wrapper = Wrapper()

    resp = kap_wrapper.get("https://www.kap.org.tr/tr/fon-bilgileri/genel/tkf-tacirler-portfoy-hisse-senedi-fonu-hisse-senedi-yogun-fon")

    print(resp)