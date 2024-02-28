1. **Pyzbar**
   
https://pypi.org/project/pyzbar/

Works with PIL / Pillow images, OpenCV / imageio / numpy ndarrays, and raw bytes.

Decodes locations of barcodes.

No dependencies, other than the zbar library itself.

**Example usage**:
```
>>> from pyzbar.pyzbar import decode
>>> from PIL import Image
>>> decode(Image.open('pyzbar/tests/code128.png'))
```
