from llm import get_domain_status, rag, social


def bot_rag(query):
    domain = get_domain_status(query).text
    if "IN-DOMAIN" in domain:
        return rag(query).text
    if "OUT-DOMAIN" in domain:
        return "Câu hỏi không nằm trong phạm vi tư vấn, chi tiết liên hệ phòng CTSV của UIT"
    if "SOCIAL" in domain:
        return social(query).text
    if "ABUSE" in domain:
        return "Bạn đang lạm dụng hệ thống, mời hỏi câu khác"
