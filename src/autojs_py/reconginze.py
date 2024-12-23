import cv2
import numpy as np

def template_match(image_path, template_path, threshold=0.8):
    # 加载主图像和模板图像
    # Check if image_path is a file path or a numpy array
    if isinstance(image_path, str):
        image = cv2.imread(image_path)
    elif isinstance(image_path, np.ndarray):
        image = image_path
    else:
        raise ValueError("image_path must be a file path or a numpy array")


    template = cv2.imread(template_path)
    template_height, template_width = template.shape[:2]

    # 执行模板匹配
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # 找到所有匹配值高于阈值的位置
    locations = np.where(result >= threshold)
    matches = []

    # 将匹配的位置添加到列表中
    for point in zip(*locations[::-1]):  # 反转坐标
        matches.append((point[0], point[1], template_width, template_height))
        cv2.rectangle(image, point, (point[0] + template_width, point[1] + template_height), (0, 255, 0), 2)


    return matches,image

if __name__ == '__main__':
# 使用示例
    matching_positions ,image = template_match('screenshot.png', 'template.png', threshold=0.8)

    # 打印匹配的位置
    for pos in matching_positions:
        # 展示图片比较结果 (可选)
        print(f"匹配位置: {pos}")

        # 显示结果
    cv2.imshow('Detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()