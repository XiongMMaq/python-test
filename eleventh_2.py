#!/usr/local/bin/python3

#exception 处理

'''
1、try子句中如果没有抛出异常，则else会执行，except不会执行，finally总会被执行
2、try子句中如果抛出了异常，则else不会执行，except会执行，finally总会被执行
3、except可以有多个（两种方式）：
    方式一：
    except (RuntimeError, TypeError, NameError):
            pass
    
    方式二：
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


'''
def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")

print(divide(2,0))