import io
from project import BaseConfig
from project.modules.s3Connect import s3connection

# 1. 업로드 파일 이미지 판별
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
def allowed_img(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# 2. PIL로 파일 열기
def pilimg(file):
    try:
        import Image
    except ImportError:
        from PIL import Image
    image = Image.open(file)
    return image

# 3. 리사이징 이미지 s3로 보내기, url 리턴
def pilimgs3(pimg, w, h, s3key, sid):
    s3 = s3connection()
    s3img = pilimg(pimg).resize((w,h))
    buffer = io.BytesIO()
    s3img = s3img.convert("RGB")
    s3img.save(buffer, "JPEG")
    buffer.seek(0)
    s3.put_object(
        Body = buffer,
        Bucket = 'heradeebucket',
        Key = s3key + str(sid),
        ContentType = 'image/jpeg'
    )
    return BaseConfig.S3_URL + '/' + s3key + str(sid)