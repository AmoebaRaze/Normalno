from api import predict, app
from api.functions import download_image
from config import PORT
import os
import uvicorn

model = predict.load_model('C:\\Users\\Arbazakark\\Desktop\\NSFW_Detection_API-master\\nsfw_detector\\nsfw_model.h5')

def f():
    image = "C:\\Users\\Arbazakark\\Desktop\\NSFW_Detection_API-master\\images\\1.png" #<-----
    results = predict.classify(model, image)
    os.remove(image)

    hentai = results['data']['hentai']
    sexy = results['data']['sexy']
    porn = results['data']['porn']
    drawings = results['data']['drawings']
    neutral = results['data']['neutral']

    if neutral >= 25:
        results['data']['is_nsfw'] = False
        return results
    elif (sexy + porn + hentai) >= 70:
        results['data']['is_nsfw'] = True
        return results
    elif drawings >= 40:
        results['data']['is_nsfw'] = False
        return results
    else:
        results['data']['is_nsfw'] = False
        return results


res = f()
print(res)


#
# @app.get("/")
# async def detect_nsfw(url="https://incanto.eu/upload/webp/resize_cache/fff/9999_1430_1/fffe859fe56cf89f62061c01c24c932f.webp"):
#     if not url:
#         return {"ERROR": "URL PARAMETER EMPTY"}
#     image = await download_image(url)
#     if not image:
#         return {"ERROR": "IMAGE SIZE TOO LARGE OR INCORRECT URL"}
#     results = predict.classify(model, image)
#     os.remove(image)
#     hentai = results['data']['hentai']
#     sexy = results['data']['sexy']
#     porn = results['data']['porn']
#     drawings = results['data']['drawings']
#     neutral = results['data']['neutral']
#     if neutral >= 25:
#         results['data']['is_nsfw'] = False
#         return results
#     elif (sexy + porn + hentai) >= 70:
#         results['data']['is_nsfw'] = True
#         return results
#     elif drawings >= 40:
#         results['data']['is_nsfw'] = False
#         return results
#     else:
#         results['data']['is_nsfw'] = False
#         return results

#
# if __name__ == "__main__":
#     uvicorn.run("api:app", host="localhost", port=PORT, log_level="info")

#
# #https://i1.sndcdn.com/avatars-000343516318-241lzu-t240x240.jpg
