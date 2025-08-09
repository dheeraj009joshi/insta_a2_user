from instagrapi import Client

cl=Client()
cl.login_by_sessionid("72834751862%3A8Iod3xoTDGeHnE%3A0%3AAYddVMv0sxQgcXigTPcR6Ambp1DkiYT236Id7A02Gw")
print(cl.get_settings())
user=cl.user__info_by_username_a2("chandigarhuniversity")

print(user)