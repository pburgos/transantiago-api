from sqlalchemy import Column
from sqlalchemy.types import Date, String

from scl_transport.gtfsdb.gtfsdb import config
from scl_transport.gtfsdb.gtfsdb.model.base import Base


class FeedInfo(Base):
    datasource = config.DATASOURCE_GTFS
    filename = 'feed_info.txt'

    __tablename__ = 'feed_info'
    __table_args__ = {'extend_existing': True}

    feed_publisher_name = Column(String(255), primary_key=True)
    feed_publisher_url = Column(String(255), nullable=False)
    feed_lang = Column(String(255), nullable=False)
    feed_start_date = Column(Date)
    feed_end_date = Column(Date)
    feed_version = Column(String(255))
    feed_license = Column(String(255))
