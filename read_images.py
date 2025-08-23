from PIL import Image
import glob
import matplotlib.pyplot as plt
from collections import Counter

class ImageMetadata:
    def __init__(self, lens_model, focal_length, iso, shutter_speed, apeture):
        self.lens_model = lens_model
        self.focal_length = focal_length
        self.iso = iso
        self.shutter_speed = shutter_speed
        self.apeture = apeture

    def info(self):
        print(f"{self.focal_length} : {self.iso} : {self.shutter_speed} : {self.apeture}")


def create_focal_length_histogram(image_metadatas, lens_model, figure_name):    
    # Filter by kit lens
    image_metadatas = [x for x in image_metadatas if x.lens_model == lens_model]
    
    # Sort by focal length
    image_metadatas.sort(key=lambda x: x.focal_length)
    focal_lengths = []
    for image_metadata in image_metadatas:
        focal_lengths.append(image_metadata.focal_length)

    # Create histogram
    plt.figure()
    plt.hist(focal_lengths, bins=25, edgecolor="black")
    plt.title("Focal Length Histogram")
    plt.xlabel("Focal Length (mm)")
    plt.ylabel("Frequency")
    plt.savefig(f"graphs/{figure_name}.png", dpi=300)
    
    
def create_iso_barchart(image_metadatas, lens_model, figure_name):
    # Filter by kit lens
    image_metadatas = [x for x in image_metadatas if x.lens_model == lens_model]
    
    # Sort by iso
    image_metadatas.sort(key=lambda x: x.iso)
    isos = []
    for image_metadata in image_metadatas:
        isos.append(image_metadata.iso)
        
    # Count the frequency of each ISO value
    iso_counts = Counter(isos)
    iso_values = sorted(iso_counts.keys())
    frequencies = [iso_counts[iso] for iso in iso_values]
    iso_strings = [str(x) for x in iso_values]

    # Create bar chart
    plt.figure()
    plt.bar(iso_strings, frequencies, edgecolor="black")
    plt.title(f"ISO Bar Chart")
    plt.xlabel("ISO")
    plt.ylabel("Frequency")
    plt.xticks(iso_strings)
    plt.savefig(f"graphs/{figure_name}.png", dpi=300)
    

def create_shutter_speed_histogram(image_metadatas, lens_model, figure_name):
    # Filter by kit lens
    image_metadatas = [x for x in image_metadatas if x.lens_model == lens_model]
    
    # Sort by shutter speed
    image_metadatas.sort(key=lambda x: x.shutter_speed)
    shutter_speeds = []
    for image_metadata in image_metadatas:
        shutter_speeds.append(image_metadata.shutter_speed)

    # Create histogram
    plt.figure()
    plt.hist(shutter_speeds, bins=75, edgecolor="black")
    plt.title("Shutter Speed Histogram")
    plt.xlabel("Shutter Speed (s)")
    plt.ylabel("Frequency")
    plt.savefig(f"graphs/{figure_name}.png", dpi=300)
    

def create_apeture_barchart(image_metadatas, lens_model, figure_name):
    # Filter by kit lens
    image_metadatas = [x for x in image_metadatas if x.lens_model == lens_model]
    
    # Sort by apeture
    image_metadatas.sort(key=lambda x: x.apeture)
    apetures = []
    for image_metadata in image_metadatas:
        apetures.append(image_metadata.apeture)

    # Count the frequency of each ISO value
    apeture_counts = Counter(apetures)
    apeture_values = sorted(apeture_counts.keys())
    frequencies = [apeture_counts[apeture] for apeture in apeture_values]
    apeture_strings = [str(x) for x in apeture_values]

    # Create bar chart
    plt.figure()
    plt.bar(apeture_strings, frequencies, edgecolor="black")
    plt.title(f"Apeture Bar Chart")
    plt.xlabel("Apeture")
    plt.ylabel("Frequency")
    plt.xticks(apeture_strings)
    plt.savefig(f"graphs/{figure_name}.png", dpi=300)


def create_shutter_speed_apeture_iso_scatter(image_metadatas, lens_model, figure_name):
    # Filter by kit lens
    image_metadatas = [x for x in image_metadatas if x.lens_model == lens_model]
    
    # Sort by shutter speed
    image_metadatas.sort(key=lambda x: x.shutter_speed)
    shutter_speeds = []
    for image_metadata in image_metadatas:
        shutter_speeds.append(image_metadata.shutter_speed)
        
    # Sort by apeture
    image_metadatas.sort(key=lambda x: x.apeture)
    apetures = []
    for image_metadata in image_metadatas:
        apetures.append(image_metadata.apeture)
        
    # Calculate the sizes
    current_shutter_speed = -1.0
    current_apeture = -1.0
    current_size = 0.0
    sizes = []
    
    for i in range(len(apetures)):
        if ((apetures[i] != current_apeture or shutter_speeds[i] != current_shutter_speed) and current_shutter_speed != -1.0 and current_apeture != -1.0):
            sizes.append(current_size + 30)
            current_size = 0.0
            current_shutter_speed = -1.0
            current_apeture = -1.0
        else:
            current_size = current_size + 1.0
            current_shutter_speed = shutter_speeds[i]
            current_apeture = apetures[i]
            sizes.append((current_size * 3) + 30)
        
    # Sort by iso
    image_metadatas.sort(key=lambda x: x.iso)
    isos = []
    for image_metadata in image_metadatas:
        isos.append(image_metadata.iso)

    # Create bar chart
    plt.figure()
    plt.scatter(shutter_speeds, apetures, c=isos, cmap='managua', s=sizes)
    plt.title(f"Shutter Speed / Apeture / ISO Scatter")
    plt.xlabel("Shutter Speed (s)")
    plt.ylabel("Apeture")
    plt.colorbar(fraction=0.05)
    plt.grid()
    plt.savefig(f"graphs/{figure_name}.png", dpi=300)
    

def create_shutter_speed_apeture_focal_length_scatter(image_metadatas, lens_model, figure_name):
    # Filter by kit lens
    image_metadatas = [x for x in image_metadatas if x.lens_model == lens_model]
    
    # Sort by shutter speed
    image_metadatas.sort(key=lambda x: x.shutter_speed)
    shutter_speeds = []
    for image_metadata in image_metadatas:
        shutter_speeds.append(image_metadata.shutter_speed)
        
    # Sort by apeture
    image_metadatas.sort(key=lambda x: x.apeture)
    apetures = []
    for image_metadata in image_metadatas:
        apetures.append(image_metadata.apeture)
        
    # Sort by focal length
    image_metadatas.sort(key=lambda x: x.focal_length)
    focal_lengths = []
    for image_metadata in image_metadatas:
        focal_lengths.append(image_metadata.focal_length)
        
    # Calculate the sizes
    current_shutter_speed = -1.0
    current_apeture = -1.0
    current_size = 0.0
    sizes = []
    
    for i in range(len(apetures)):
        if ((apetures[i] != current_apeture or shutter_speeds[i] != current_shutter_speed) and current_shutter_speed != -1.0 and current_apeture != -1.0):
            sizes.append(current_size + 30)
            current_size = 0.0
            current_shutter_speed = -1.0
            current_apeture = -1.0
        else:
            current_size = current_size + 1.0
            current_shutter_speed = shutter_speeds[i]
            current_apeture = apetures[i]
            sizes.append((current_size * 3)  + 30)

    # Create bar chart
    plt.figure()
    plt.scatter(shutter_speeds, apetures, c=focal_lengths, cmap='managua', s=sizes)
    plt.title(f"Shutter Speed / Apeture / Focal Length Scatter")
    plt.xlabel("Shutter Speed (s)")
    plt.ylabel("Apeture")
    plt.colorbar(fraction=0.05)
    plt.grid()
    plt.savefig(f"graphs/{figure_name}.png", dpi=300)


if __name__ == "__main__":
    # plt basic params
    plt.rcParams["figure.figsize"] = (18, 10)
    
    image_metadatas = []

    # Read the metadata from the images
    for image_name in glob.glob("images/*.JPG"):
        image = Image.open(image_name)
        image_exif = image.getexif()
        image_metadata = ImageMetadata(str(image_exif.get_ifd(34665).get(42036)),
                                float(image_exif.get_ifd(34665).get(37386)),
                                int(image_exif.get_ifd(34665).get(34855)),
                                float(image_exif.get_ifd(34665).get(33434)),
                                float(image_exif.get_ifd(34665).get(33437)))
        image_metadatas.append(image_metadata)
    
    create_focal_length_histogram(image_metadatas, "EF-S18-55mm f/3.5-5.6 IS II", "FocalLengthHistogramKit")
    create_focal_length_histogram(image_metadatas, "EF-S55-250mm f/4-5.6 IS STM", "FocalLengthHistogramTele")
    
    create_iso_barchart(image_metadatas, "EF-S18-55mm f/3.5-5.6 IS II", "ISOBarChartKit")
    create_iso_barchart(image_metadatas, "EF-S55-250mm f/4-5.6 IS STM", "ISOBarChartTele")
    
    create_shutter_speed_histogram(image_metadatas, "EF-S18-55mm f/3.5-5.6 IS II", "ShutterSpeedHistogramKit")
    create_shutter_speed_histogram(image_metadatas, "EF-S55-250mm f/4-5.6 IS STM", "ShutterSpeedHistogramTele")
    
    create_apeture_barchart(image_metadatas, "EF-S18-55mm f/3.5-5.6 IS II", "ApetureBarChartKit")
    create_apeture_barchart(image_metadatas, "EF-S55-250mm f/4-5.6 IS STM", "ApetureBarChartTele")
    
    create_shutter_speed_apeture_iso_scatter(image_metadatas, "EF-S18-55mm f/3.5-5.6 IS II", "ApetureShutterISOScatterKit")
    create_shutter_speed_apeture_iso_scatter(image_metadatas, "EF-S55-250mm f/4-5.6 IS STM", "ApetureShutterISOScatterTele")
    
    create_shutter_speed_apeture_focal_length_scatter(image_metadatas, "EF-S18-55mm f/3.5-5.6 IS II", "ApetureShutterFocalScatterKit")
    create_shutter_speed_apeture_focal_length_scatter(image_metadatas, "EF-S55-250mm f/4-5.6 IS STM", "ApetureShutterFocalScatterTele")
