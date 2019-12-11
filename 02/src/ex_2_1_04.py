def div(x,y):
    try:
        return x/y
    # except TypeError:
    #     print ("TypeError")
    # except ZeroDivisionError:
    #     print("Zero Division")
    except (TypeError, ZeroDivisionError) as e:
        print(e)
        print(e.args)
        print(type(e))
    else:
        pass
    finally:
        pass

div(5,0)