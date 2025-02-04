from .database import db, ContentRegistry
from .config import Config
from datetime import datetime

def is_duplicate(content_hash):
    existing = db.session.query(ContentRegistry).get(content_hash)
    if existing:
        time_diff = datetime.now() - existing.last_sent
        if time_diff < Config.DUPLICATION_RULES['time_window']:
            if existing.sent_count >= Config.DUPLICATION_RULES['allowed_repeats']:
                return True
    return False
    
    def is_duplicate(content_hash):
    # هنا سيكون تنفيذ للتحقق مما إذا كان المحتوى مكررًا
    pass