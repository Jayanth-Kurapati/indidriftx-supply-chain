from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    severity,
    shock_data,
    consumer_data,
    investment_data,
    summary_data
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "IndiDriftX Executive Intelligence Report",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            f"Scenario Severity: {severity}%",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            summary_data["bottom_line"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Industry Impact Analysis",
            styles["Heading1"]
        )
    )

    for industry in shock_data["industries"]:

        content.append(
            Paragraph(
                f"""
                <b>{industry['name']}</b><br/>
                Impact: {industry['impact_level']}<br/>
                Dependency: {industry['dependency']}%<br/>
                Revenue Loss: ${industry['revenue_loss_bn']}B
                """,
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    content.append(
        Paragraph(
            "Consumer Impact Analysis",
            styles["Heading1"]
        )
    )

    for product in consumer_data["products"]:

        content.append(
            Paragraph(
                f"""
                <b>{product['product']}</b><br/>
                Price Increase: {product['price_increase_pct']}%<br/>
                New Price: ${product['new_avg_price_usd']}<br/>
                Risk: {product['shortage_risk']}
                """,
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    content.append(
        Paragraph(
            "Investment Intelligence",
            styles["Heading1"]
        )
    )

    for sector in investment_data["sectors"]:

        content.append(
            Paragraph(
                f"""
                <b>{sector['sector']}</b><br/>
                Signal: {sector['signal']}<br/>
                Risk Score: {sector['risk_score']}<br/>
                Opportunity Score: {sector['opportunity_score']}<br/>
                Action: {sector['action']}
                """,
                styles["BodyText"]
            )
        )

    doc.build(content)

    buffer.seek(0)

    return buffer