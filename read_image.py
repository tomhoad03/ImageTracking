from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import TAGS

# path to the image or video
imagename = "images/IMG_7742.JPG"

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
img_exif = image.getexif()
for ifd_key, ifd_value in img_exif.get_ifd(ExifTags.Base.ExifOffset).items():

    ifd_tag_name = ExifTags.TAGS.get(ifd_key, ifd_key)
    print(f" {ifd_tag_name}: {ifd_value}")

IFD_CODE_LOOKUP = {i.value: i.name for i in ExifTags.IFD}

for tag_code, value in img_exif.items():

    # if the tag is an IFD block, nest into it
    if tag_code in IFD_CODE_LOOKUP:

        ifd_tag_name = IFD_CODE_LOOKUP[tag_code]
        print(f"IFD '{ifd_tag_name}' (code {tag_code}):")
        ifd_data = img_exif.get_ifd(tag_code).items()

        for nested_key, nested_value in ifd_data:

            nested_tag_name = ExifTags.GPSTAGS.get(nested_key, None) or ExifTags.TAGS.get(nested_key, None) or nested_key
            print(f"  {nested_tag_name} : {nested_key} : {nested_value}")

    else:

        # root-level tag
        print(f"{ExifTags.TAGS.get(tag_code)}: {value}")