import cv2 as cv


my_image = cv.imread(cv.samples.findFile("cat.jpg"))


# if my_image is None:
#     sys.exit("Your image is not found")
# cv.imshow("Your image", my_image)
# k = cv.waitKey(0)


b, g, r = cv.split(my_image)
green_image = g
# green_image = my_image[:, :, 1]

# cv.imshow("Green image", green_image)
# k = cv.waitKey(0)



clone1 = green_image.copy()
clone2 = green_image.copy()

# cv.imshow("clone", clone1)
# k = cv.waitKey(0)


min_value, max_value, min_loc, max_loc = cv.minMaxLoc(green_image)
print(f"Значения в зелёном изображении:\n"
      f"Минимальное: {min_value}, максимальное: {max_value}\n"
      f"Позиция минимального: {min_loc}, позиция максимального: {max_loc}")


thresh = int(abs((max_value - min_value) / 2.0))
# print(thresh)

clone1[:, :] = thresh
# print(clone1)

clone2[:, :] = 0
# print(clone2)


cv.compare(green_image, clone1, cv.CMP_GE, clone2)
# print(clone2)
# cv.imshow("Result", clone2)
# k = cv.waitKey(0)



cv.subtract(green_image, thresh / 2, green_image, clone2)
# print(green_image)


cv.imshow("Result", green_image)
k = cv.waitKey(0)
# if k == ord("s"):
#     cv.imwrite("subtract.jpg", green_image)