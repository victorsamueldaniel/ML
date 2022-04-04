#%%
import pandas as pd

#%%
def change_to_cat(my_df,threshold = 5):
    '''
    function that takes a dataframe and an integer
    and outputs a two-list containging:
    a copy of the dataframe with column types changed to "category" if the amount of different values is lower or equal to the integer
    a dataframe containing all the unique values from original dataframe
    '''
    temp_df = my_df.copy()
    
    #creation of copy with types changed to "category"
    cat_var = [col for col in temp_df.columns if ( (len(temp_df[col].unique()) <=threshold) or (temp_df[col].dtype=='O') )]  
    temp_df[cat_var]=temp_df[cat_var].astype("category")

    #creation of the df with unique values only
    temp_df_unique = pd.DataFrame.from_dict({var : sorted(list(temp_df[var].unique()), key= lambda x: str(x)) for var in cat_var}, orient='index').T
    return [temp_df,temp_df_unique]
# %%
def check_almost_duplicates(df):
    '''
    df must be output of change_to_cat[0]
    '''
    df_temp=pd.DataFrame()
    from difflib import SequenceMatcher
    for col in df.columns:
        series_of_column = df[col]
        boolean_series_of_column = pd.DataFrame({col : [False]*len(df)},index=df.index)[col]
        for iterating_line in range(len(df)-1):
            for comparing_line in range(iterating_line+1,len(df)):
                if SequenceMatcher(None, series_of_column.iloc[iterating_line],series_of_column.iloc[comparing_line]).ratio()>0.7:
                    boolean_series_of_column.iloc[iterating_line]=True
                    boolean_series_of_column.iloc[comparing_line]=True
        df_temp = pd.concat([df_temp, df[boolean_series_of_column]], axis = 1)
    return df_temp
# %%
df = pd.DataFrame({'var': ['caggle','ciggle'],'vour': ['caggle','cigascxyxc gggle']})
# %%
check_almost_duplicates(df)
# %%
pd.concat([pd.DataFrame(),df], axis = 1)
# %%
df.index
# %%
