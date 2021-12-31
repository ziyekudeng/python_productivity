from PyPDF4 import PdfFileReader, PdfFileWriter

'''
PyPDF2库合并pdf后乱码,可以通过更换pyPDF4这个库解决这个问题
'''

def watermark(pdfWithoutWatermark, watermarkfile, pdfWithWatermark):
    # 准备合并后的文件对象
    pdfWriter = PdfFileWriter()
    
    watermark_file = open(watermarkfile, 'rb')
    watermarkpage = PdfFileReader(watermark_file, strict=False)   
    # 打开需要增加水印的文件
    pdfWithoutWatermark_file = open(pdfWithoutWatermark, 'rb')
    pdf_file = PdfFileReader(pdfWithoutWatermark_file, strict=False)

    for i in range(pdf_file.getNumPages()):
        # 从第一页开始处理
        page = pdf_file.getPage(i)
        # 合并水印和当前页
        page.mergePage(watermarkpage.getPage(0))
        # 将合并后的PDF文件写入新的文件
        pdfWriter.addPage(page)
    
    # 写入新的PDF文件
    pdfWithWatermark_file = open(pdfWithWatermark, 'wb')
    pdfWriter.write(pdfWithWatermark_file)
    
    watermark_file.close()
    pdfWithoutWatermark_file.close()
    pdfWithWatermark_file.close()

if __name__ == "__main__":
    pdf_without_watermark = "python_productivity\文章30代码\合同.pdf"
    pdf_with_watermark = "python_productivity\文章30代码\加水印合同.pdf"
    watermark_file = "python_productivity\文章30代码\水印.pdf"

    watermark(pdf_without_watermark, watermark_file, pdf_with_watermark)
