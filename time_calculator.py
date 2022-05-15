def proc_start(start):
    
    x = start.split(':')
    x[1] = x[1].split()
    x.extend(x[1])
    del x[1]
    
    if x[2] == "PM":
        hr = 12+int(x[0])
    else:
        hr = int(x[0])
    
    base = [str(hr), x[1]]
    return base

def add_to_base(base, duration):
    duration = duration.split(':')
    
    # Process Minutes
    mt = int(base[1])+int(duration[1])
    mt_60 = int(mt/60)
    mt_remain = mt%60    

    
    # Process Hours
    hr = int(base[0])+int(duration[0]) + mt_60
    days = int(hr/24)
    hours = hr%24
    
    added_time = [days, hours, mt_remain]   
     
 
    return added_time


def print_time(added_time, w_day = None):
    
    # Check length of minutes. Need to have 2 digits
    if added_time[2] < 10:
        minutes = "0" + str(added_time[2])
    else:
        minutes = str(added_time[2])
    
    
    # AM or PM
    am_pm = None
    hr_am_pm = None
    
    
    if added_time[1] < 12:
        am_pm = "AM"
        hr_am_pm = added_time[1]
    else:
        am_pm = "PM"
        hr_am_pm = added_time[1] - 12
    
    # Make sure that "hr_am_pm" is not zero and convert to string
    if hr_am_pm == 0:
        hr_am_pm = str(12)
    else:
        hr_am_pm = str(hr_am_pm)
        
        
        
        
    # Today, the next day, or n-days
    n_days = None
    if added_time[0] == 0:
        n_days = ""
    elif added_time[0] == 1:
        n_days = " (next day)"
    else:
        n_days = " (" + str(added_time[0]) + " days later)"
      
    
    # Check if week day is required
    if w_day != None:
        wk_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        wk_d = wk_days.index(w_day.lower().capitalize()) + added_time[0]
        wk_d_no = wk_d%7
        
        # Assemble final message
        hr_final = hr_am_pm + ":" + minutes + ' ' + am_pm +', ' + wk_days[wk_d_no] + n_days
        
    else:
        # Assemble final message
        hr_final = hr_am_pm + ":" + minutes + ' ' + am_pm + n_days
    
    return hr_final


def add_time(start, duration, w_day = None):
    base = 0
    
    base = proc_start(start)
    
    added_time = add_to_base(base, duration)
    
    new_time = print_time(added_time, w_day)  




    return new_time