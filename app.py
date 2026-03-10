# @title أداة تحويل سوفتات صن بلس (Daky Converter)
import os
from google.colab import files

print("1. ارفع السوفت الأصلي للجهاز (Original)")
uploaded_org = files.upload()
org_name = list(uploaded_org.keys())[0]

print("2. ارفع السوفت الجديد المراد التحويل إليه (Target)")
uploaded_new = files.upload()
new_name = list(uploaded_new.keys())[0]

# العنوان الذي حددته أنت: 0x1A000
offset = 0x1A000
length = 0x10  # طول كود الـ ID (16 بايت)

try:
    with open(org_name, "rb") as f:
        f.seek(offset)
        id_value = f.read(length)
    
    with open(new_name, "rb") as f:
        target_data = bytearray(f.read())

    # حقن القيمة في العنوان 1A000
    target_data[offset:offset+length] = id_value
    
    output_name = "Converted_By_Gemini.bin"
    with open(output_name, "wb") as f:
        f.write(target_data)

    print(f"\n✅ تمت العملية بنجاح!")
    print(f"تم سحب الـ ID من العنوان {hex(offset)} وحقنه في السوفت الجديد.")
    files.download(output_name)

except Exception as e:
    print(f"❌ حدث خطأ: {e}")