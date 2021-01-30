import dash_html_components as html

thematter_link = 'https://thematter.co/social/lifestyle/instant-noodles-review-6-brand/121500'

layout = html.Div([
    html.H1('ขอขอบคุณท่านผู้ชมทุกคนที่เข้ามาชมเว็บนี้นะครับ'),
    html.P('เว็บนี้ผมทำเพื่อฝึก skill ด้าน data visualization และการวิเคราะห์ด้วยภาพที่ได้เรียนใน 2603646 information visualization, chulalongkorn university เท่านั้น มิได้มีเจตนาโจมตีแบรนด์ต่างๆแต่อย่างใด'),
    html.H1('ขอขอบคุณ data จากสำนักข่าว The MATTER คอลัมน์ข่าว "รีวิวบะหมี่กึ่งสำเร็จรูปไทย 6 แบรนด์ จากคนเงินเดือนใกล้หมด 24/8/2020"'),
    html.A('source', href=thematter_link, rel="noopener noreferrer", target='_blank'),
    html.H1('ขอขอบคุณ อาจารย์ ภูริพันธุ์ รุจิขจร สำหรับคำปรึกษาการทำ visualization'),
    html.H1('สุดท้ายขอขอบคุณเพื่อนๆทุกคนที่แสดงความคิดเห็นสำหรับการนำไปพัฒนาเว็บต่อไปในอนาคต'),
    html.H3('1/30/2021')

],
    id='ending'
)