import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# FLO datasetini Genel Kapsamda İnceleyelim
df = pd.read_csv(r"C:\Users\sanbe\OneDrive\Masaüstü\PythonProgramlama\Datasets\flo_data_20k.csv")

# Dataset genel bilgileri
print(df.head())
print(df.columns)
df.info()
print(df.describe())
print(df.isnull().any())

################################################
# Değişken Tiplerini Sınıflandırma
################################################

# Kategorik Değişkenler:
# masterCategory, subCategory, articleType, baseColour,
# season, usage, productDisplayName, salesChannel

# Sayısal Değişkenler:
# year, price, discountRate

cat_cols = [col for col in df.columns if df[col].dtype == "object"]
num_cols = [col for col in df.columns if df[col].dtype in ["int64", "float64"]]

print("Kategorik Değişkenler:", cat_cols)
print("Sayısal Değişkenler:", num_cols)

################################################
# Kategorik Değişkenler = ['master_id', 'order_channel', 'last_order_channel', 
# 'first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline',
#  'interested_in_categories_12']

# Sayısal Değişkenler = ['order_num_total_ever_online', 'order_num_total_ever_offline',
# 'customer_value_total_ever_online', 'customer_value_total_ever_offline', 'interested_in_categories_12']
################################################

#Kategorik Değişken Analizi
def cat_summary(dataframe, col_name):
    
    print(pd.DataFrame({
        col_name: dataframe[col_name].value_counts(),
        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)
    }))
    
    print("###################################")

print(cat_summary(df, "master_id"))
print(cat_summary(df, "order_channel"))
print(cat_summary(df, "last_order_channel"))
print(cat_summary(df, "first_order_date"))
print(cat_summary(df, "last_order_date"))
print(cat_summary(df, "last_order_date_online"))
print(cat_summary(df, "last_order_date_offline"))

#Sayısal Değişken Analizi
def num_summary(dataframe, num_name):
    quantiles = [ 0.20, 0.50, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[num_name].describe(quantiles).T)
    print("###################################")

print(num_summary(df, "order_num_total_ever_online"))
print(num_summary(df, "order_num_total_ever_offline"))
print(num_summary(df, "customer_value_total_ever_online"))
print(num_summary(df, "customer_value_total_ever_offline"))





#Online ve Offline Toplam Harcama Karşılaştırması
online = df["customer_value_total_ever_online"].sum()
offline = df["customer_value_total_ever_offline"].sum()

plt.bar(["Online","Offline"], [online, offline])
plt.title("Online vs Offline Toplam Harcama")
plt.show()



#Total Order ve Total Value Değişkenleri Oluşturduk çünkü online ve offline toplam sipariş sayısı ve toplam müşteri değeri değişkenlerini tek bir değişkende toplamak istiyoruz. Böylece müşterilerin toplam sipariş sayısı ve toplam müşteri değeri hakkında daha genel bir bilgiye sahip olabiliriz.  
df["total_order"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]

df["total_value"] = df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"]


#Korelasyon Analizi
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap="RdBu")
plt.show()