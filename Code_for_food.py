
import numpy as np
import random

veg_dishes = {0:'palak paneer',1:'palak aloo',2:'aloo matar',\
                 3:'pav bhaji', 4:'shahi paneer', 5:'paneer butter masala',6:'malai paneer',\
                 7:'veg pulao',8:'Salad',9:'Pasta/Spegetti',10:'aloo Bhindi',11:'aloo gobi',\
                 12:'kadhai/paneer do pyaza',13:'egg curry',14:'Aloo bellpepper'}

    
veg_dishes2 = veg_dishes.copy()
Nonveg_dish = {0:'Biryani',1:'Kadhai/curry chicken',2:'chicken butter masala',3:'shahi/malai chicken',
               4:'grilled chicken'}
Nonveg_dish2 = Nonveg_dish.copy()
Dal = {0:'Moong Masoor',1:'Toor',2:'chola',3:'Rajma',4:'Urad Chana',5:'chana dal',6:'plain rice with dal',7:'none'}
Dal2 = Dal.copy()


veg_nonveg_probs = [0.85, 0.15]
veg_dal_prob_for_second_dish = [0.1, 0.9] #when veg [0.4 0.6] when non veg  

status = 'free' # if super busy type busy


sample_dish1 = []
sample_dish2 = []
for i in range(13):
    
    veg_noveg_num = np.random.rand(1)
    veg_dal_num = np.random.rand(1)
    
    if veg_noveg_num <=0.85:
        key1 = random.sample(veg_dishes2.keys(), 1)
        sample_dish1 += [veg_dishes2[k] for k in key1]
        veg_dishes2.pop(int(np.array(key1)))

        if veg_dal_num<=0.1:
            key2 = random.sample(veg_dishes2.keys(), 1)
            sample_dish2 += [veg_dishes2[k] for k in key2]
            veg_dishes2.pop(int(np.array(key2)))
        else:
            key2 = random.sample(Dal2.keys(), 1)
            sample_dish2+= [Dal2[k] for k in key2]
            
    
    
    else:
        key1 = random.sample(Nonveg_dish2.keys(), 1)
        sample_dish1 += [Nonveg_dish2[k] for k in key1]
        Nonveg_dish2.pop(int(np.array(key1)))

        if veg_dal_num<=0.4:
            key2 = random.sample(veg_dishes2.keys(), 1)
            sample_dish2+= [veg_dishes2[k] for k in key2]
            veg_dishes2.pop(int(np.array(key2)))
        else:
            key2 = random.sample(Dal2.keys(), 1)
            sample_dish2 += [Dal2[k] for k in key2]
            
for i in range(13):
    print(i,  sample_dish1[i],' ' * (25 - len(sample_dish1[i])-len(str(i))),sample_dish2[i])
  
    