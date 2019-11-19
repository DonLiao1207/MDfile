## MATLAB Memo
##### SQL JDBC CONNECT NOT WORK?

```
writedata = table(111,'VariableNames',{'pca';});
rows = sqlread(conn,tablename);
tablename = 'postgres.oven.inference';
sqlwrite(conn, tablename,  writedata);
rows = sqlread(conn,tablename);
query = 'INSERT INTO oven.inference (PCA) VALUES (100)';
pdata = fetch(conn, query);
insert_str= ['INSERT INTO oven.inference (id, t2limit, spelimit, t2, spe, cv, rul) VALUES (', id, ',', T2Limit, ',',  SPELimit,  ',', T2, ',',  SPE, ',',  CV, ',',  RUL, ')']


```

##### quotes

```
str "" 用 ["A"+"B"+....]
str '' 用 ['A','B',....]
```

##### MATLAB Runtime    
```
./run.sh ./run_Inference.sh /usr/local/MATLAB/R2019a/
(MCRdir)
```

#####  Linux run m file
```
matlab -nodesktop -nosplash -r 
```

##### MATLAB UDP toolbox
```
Simulink.
Instrument Control Toolbox. 
/home/don/PHM_Learning/Orisol/Matlab_Code/Matlab_Inference/Inference/for_redistribution_files_only/run_Inference.sh /usr/local/MATLAB/MATLAB_Runtime/v96/
```