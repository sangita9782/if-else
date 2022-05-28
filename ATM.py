atm_card=input("insert the card")
if atm_card=="Right side" or atm_card=="right side":
    language=input("enter language")
    if language=="english" or language=="hindi":
        pin=int(input("enter the four digit pin"))
        if pin>=1000 and pin<=9999:
            thransaction_type=input("enter thransaction")
            if  thransaction_type=="withdrawal" or thransaction_type=="Withdrawal":
                account_type=input("enter account type")
                amount=int(input("enter amount"))
                key_name=input("enter key_name")
                if amount>=500 and amount<=2000 or amount%500:
                    a=amount//2000
                    b=amount%2000
                    c=b//500
                    d=b%500
                    print("notes of 2000",a,"notes of 500,b")
                receip_money=input("enter receip money")
                if receip_money=="ok" or receip_money=="OK":
                        print("receip money")
                else:
                        print("thanks for thransaction")
            elif thransaction_type=="Balance enquiry" or thransaction_type=="balance enquiry":
                account_type=input("enter account_type")
                print("total amount")
                key_name=input("enter key_name")
                if key_name=="ok" or key_name=="OK":
                    print("thanks for balance enquiry") 
                else:
                    print("invalid key")   
            elif thransaction_type=="deposit money" or thransaction_type=="Deposit money":
                account_number=int(input("enter account number"))
                if account_number>=1000000000 and account_number<=9999999999:
                    bill_ammount=int(input("enter the bill amount"))
                    if bill_ammount>=1000000000 and bill_ammount<=9999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter key_name")
                        if key_name=="ok" or key_name=="OK":
                            print("succesfull")
                        else:
                            print("unsuccesfull")
            elif thransaction_type=="bill_pay" or thransaction_type=="Bill_pay":
                account_number=int(input("enter account_number"))
                if account_number>=1000000000 and account_number<=9999999999:
                    bill_id=int(input("enter bill_id"))
                    if bill_id>=1000000000 and bill_id<=9999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter key_name")
                        print("successfull")
                    else:
                        print("unsuccesfull")
            else:
                print("unsuccesfull")
        else:   
            print("invalid pin")
    else:
        print("no bengali language")
else:
    print("rejected")