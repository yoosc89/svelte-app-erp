from datetime import datetime
from models import Customer, CustomerDetail, User
from customer.customer_schema import CustomerCreate, CustomerUpdate
from sqlalchemy.orm import Session
from user import user_schema


def get_customer_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = ''):

    lastquery = db.query(CustomerDetail.id).filter(CustomerDetail.customer_id ==
                                                   Customer.id).order_by(CustomerDetail.id.desc()).first()
    subquery = db.query(CustomerDetail.id, CustomerDetail.body, CustomerDetail.phonenumber, CustomerDetail.create_date, User.name).outerjoin(
        User, User.id == CustomerDetail.user_id).subquery()

    customer_list = db.query(Customer.id, subquery.c.body,
                             subquery.c.create_date, subquery.c.name, subquery.c.phonenumber
                             ).outerjoin(subquery, subquery.c.id == lastquery.id
                                         ).order_by(Customer.id.desc())

    total = customer_list.distinct().count()
    customer_list = customer_list.order_by(
        Customer.create_date.desc()).offset(skip).limit(limit).distinct().all()

    return total, customer_list


def get_customer(db: Session, customer_id: int):
    customer = db.query(Customer).get(customer_id)
    return customer


def del_get_customer_list(db: Session, customer_idlist: list):
    customer_list = []
    for i in customer_idlist:
        customer_list.append(db.query(Customer).get(i.customer_id))
    return customer_list


def create_customer(db: Session, customercreate: CustomerCreate, user: user_schema.User):
    create_date = datetime.now()
    db_customer = Customer(
        create_date=create_date, user=user)
    db.add(db_customer)
    db.commit()
    customer = db.query(Customer).filter(
        Customer.user_id == user.id).order_by(Customer.id.desc()).first()
    db_customerdetail = CustomerDetail(
        name=customercreate.name, body=customercreate.body,
        phonenumber=customercreate.phonenumber, address=customercreate.address,
        addressdetail=customercreate.addressdetail, create_date=create_date, customer_id=customer.id, user=user)
    db.add(db_customerdetail)
    db.commit()

    return customer


def update_customer(db: Session, db_customer: Customer, customer_update: CustomerUpdate):
    db_customer.subject = customer_update.subject
    db_customer.content = customer_update.content
    db_customer.modify_date = datetime.now()
    db.add(db_customer)
    db.commit()


def delete_customer(db: Session, db_customer: list[Customer]):
    for i in db_customer:
        db.delete(i)
    db.commit()
