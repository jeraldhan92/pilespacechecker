# In[1]:
import pandas as pd
import numpy as np

#Importing pile spreadsheet
fileName = input("Key in file name with extension:")
dataPlot = pd.read_excel(fileName, header=1)

#Renaming column headers
headerRename = ["PCMarking","FID","RotAngle","CCX","CCY","NoA","A1","A2","A3","A4","A5","AX","AY","NoB","B0","B1","B2","B3","B4","BX","BY","BZ","NoC","C0","C1","C2","C3","CX","CY","CZ","sgdia","sgdia2","sgdiaB","sgdiaC","PileA1","PileA2","PileA3","PileA4","PileA5","PileA6","PileB1","PileB2","PileB3","PileC1","PileC2","PileC3","Corner1","Corner2"]

dataPlot.columns = headerRename

#Number of Pilecap/Pile Objects
noPileObj = dataPlot.shape[0]

#Creating pile inventory array
pileInv = pd.DataFrame(columns = ['PCMarking','CCX','CCY','sgdia'])

for x in range(noPileObj):
    if isinstance(dataPlot['CCX'].iloc[x],str):
        dataPlot['CCX'].iloc[x]=float(dataPlot['CCY'].iloc[x].replace(",",""))
    if isinstance(dataPlot['CCY'].iloc[x],str):
        dataPlot['CCY'].iloc[x]=float(dataPlot['CCY'].iloc[x].replace(",",""))

pileCounter = 0


# In[2]:


#GENERATION OF PILE INVENTORY

for x in range(noPileObj):
    if dataPlot.FID[x]==0:
        #Individual Pile
        pileCounter = pileCounter + 1

        pileDataAll = dataPlot.iloc[x,:]
        pileInvData = pileDataAll.loc[['PCMarking','CCX','CCY','sgdia']]

        pileInv = pileInv.append(pileInvData)

    elif dataPlot.FID[x]==1:
        #Pile Cap with One Row of Piles

        numberPiles = dataPlot.iloc[x,5]

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']
        pileDia = pileDataAll.loc['sgdia']

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        pileSpacing = pileDataAll.loc['A1']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        for y in range(numberPiles):
            CCX_current = CCX_origin - pileSpacing*np.sin(np.deg2rad(theta))*y
            CCY_current = CCY_origin + pileSpacing*np.cos(np.deg2rad(theta))*y

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==2:
        #Pile Cap with Two Row of Piles

        numberRows = dataPlot.iloc[x,5]
        numberPiles = numberRows * 2

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']
        pileDia = pileDataAll.loc['sgdia']

        pileSpacing = pileDataAll.loc['A1']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        CCX_origin2 = CCX_origin + pileSpacing*np.cos(np.deg2rad(theta))
        CCY_origin2 = CCY_origin + pileSpacing*np.sin(np.deg2rad(theta))

        for y in range(numberRows):
            CCX_current = CCX_origin - pileSpacing*np.sin(np.deg2rad(theta))*y
            CCY_current = CCY_origin + pileSpacing*np.cos(np.deg2rad(theta))*y

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberRows):
            CCX_current = CCX_origin2 - pileSpacing*np.sin(np.deg2rad(theta))*y
            CCY_current = CCY_origin2 + pileSpacing*np.cos(np.deg2rad(theta))*y

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==3:
        #Pile Cap with Three Row of Piles

        numberRows = dataPlot.iloc[x,5]
        numberPiles = numberRows * 3

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']
        pileDia = pileDataAll.loc['sgdia']

        pileSpacing = pileDataAll.loc['A1']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        CCX_origin2 = CCX_origin + pileSpacing*np.cos(np.deg2rad(theta))
        CCY_origin2 = CCY_origin + pileSpacing*np.sin(np.deg2rad(theta))

        CCX_origin3 = CCX_origin2 + pileSpacing*np.cos(np.deg2rad(theta))
        CCY_origin3 = CCY_origin2 + pileSpacing*np.sin(np.deg2rad(theta))


        for y in range(numberRows):
            CCX_current = CCX_origin - pileSpacing*np.sin(np.deg2rad(theta))*y
            CCY_current = CCY_origin + pileSpacing*np.cos(np.deg2rad(theta))*y

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberRows):
            CCX_current = CCX_origin2 - pileSpacing*np.sin(np.deg2rad(theta))*y
            CCY_current = CCY_origin2 + pileSpacing*np.cos(np.deg2rad(theta))*y

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberRows):
            CCX_current = CCX_origin3 - pileSpacing*np.sin(np.deg2rad(theta))*y
            CCY_current = CCY_origin3 + pileSpacing*np.cos(np.deg2rad(theta))*y

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==4:
        #Triangular Pile Cap

        numberPiles = 3

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']
        pileDia = pileDataAll.loc['sgdia']

        triA1 = pileDataAll.loc['A1']
        triA2 = pileDataAll.loc['A2']
        triA3 = pileDataAll.loc['A3']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        CCX_1 = CCX_origin - (triA1+triA2)*np.sin(np.deg2rad(theta))*y
        CCY_1 = CCY_origin + (triA1+triA2)*np.cos(np.deg2rad(theta))*y

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_1,CCY_1,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        CCX_2 = CCX_origin - (triA3)*np.cos(np.deg2rad(theta))*y
        CCY_2 = CCY_origin - (triA3)*np.sin(np.deg2rad(theta))*y

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_2,CCY_2,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        CCX_3 = CCX_origin + (triA3)*np.cos(np.deg2rad(theta))*y
        CCY_3 = CCY_origin + (triA3)*np.sin(np.deg2rad(theta))*y

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_3,CCY_3,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==5:
        #L-shaped Pile Cap

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        numberAPiles = pileDataAll.loc['NoA']
        numberBPiles = pileDataAll.loc['NoB']

        numberPiles = numberAPiles + numberBPiles - 1

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']
        pileDia = pileDataAll.loc['sgdia']
        pileDia2 = pileDataAll.loc['sgdia2']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        #Extracting Pile-Pile Spacings
        A_SpacingArray = dataPlot.iloc[x,6:5+pileDataAll.loc['NoA']]
        B_SpacingArray = dataPlot.iloc[x,15:14+pileDataAll.loc['NoB']]


        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        #Coordinates of 1st Pile
        CCX_current = CCX_origin - np.sum(A_SpacingArray)*np.sin(np.deg2rad(theta))
        CCY_current = CCY_origin + np.sum(A_SpacingArray)*np.cos(np.deg2rad(theta))

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberAPiles-1):
            CCX_current = CCX_current + A_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current - A_SpacingArray[y]*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)
        for y in range(numberBPiles-1):
            CCX_current = CCX_current + B_SpacingArray[y]*np.cos(np.deg2rad(theta))
            CCY_current = CCY_current + B_SpacingArray[y]*np.sin(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia2]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==6:
        #U-shaped Pile Cap

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        numberAPiles = pileDataAll.loc['NoA']
        numberBPiles = pileDataAll.loc['NoB']
        numberCPiles = pileDataAll.loc['NoC']

        numberPiles = numberAPiles + numberBPiles + numberCPiles - 2

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']
        pileDia = pileDataAll.loc['sgdia']
        pileDia2 = pileDataAll.loc['sgdiaB']
        pileDia3 = pileDataAll.loc['sgdiaC']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        #Extracting Pile-Pile Spacings
        A_SpacingArray = dataPlot.iloc[x,6:5+pileDataAll.loc['NoA']]
        B_SpacingArray = dataPlot.iloc[x,15:14+pileDataAll.loc['NoB']]
        C_SpacingArray = dataPlot.iloc[x,24:23+pileDataAll.loc['NoC']]

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        #Coordinates of 1st Pile
        CCX_current = CCX_origin - np.sum(A_SpacingArray)*np.sin(np.deg2rad(theta))
        CCY_current = CCY_origin + np.sum(A_SpacingArray)*np.cos(np.deg2rad(theta))

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberAPiles-1):
            pileDiaInput = pileDia
            CCX_current = CCX_current + A_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current - A_SpacingArray[y]*np.cos(np.deg2rad(theta))
            if y == numberAPiles-2:
                if pileDataAll.loc['Corner1']=="B":
                    pileDiaInput = pileDia2

            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDiaInput]],columns = ['PCMarking','CCX','CCY','sgdia'])

            pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberBPiles-1):
            pileDiaInput = pileDia2
            CCX_current = CCX_current + B_SpacingArray[y]*np.cos(np.deg2rad(theta))
            CCY_current = CCY_current + B_SpacingArray[y]*np.sin(np.deg2rad(theta))
            if y == numberBPiles-2:
                if pileDataAll.loc['Corner2']=="C":
                    pileDiaInput = pileDia3
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDiaInput]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        #Coordinates of Last Pile
        CCX_current = CCX_current - np.sum(C_SpacingArray)*np.sin(np.deg2rad(theta))
        CCY_current = CCY_current + np.sum(C_SpacingArray)*np.cos(np.deg2rad(theta))

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia3]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberCPiles-2):
            CCX_current = CCX_current + C_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current - C_SpacingArray[y]*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDia3]],columns = ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==7:
        #P-shaped Pile Cap

        #Extracting Pile Cap Group datas
        pileDataAll = dataPlot.iloc[x,:]

        numberAPiles = pileDataAll.loc['NoA']
        numberCPiles = pileDataAll.loc['NoC']

        numberPiles = numberAPiles + numberCPiles

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        #Converting Pile Diameter
        for z in range(12):
            if "Dia" in dataPlot.iloc[x,34+z]:
                pileDataAll.iloc[34+z] = int(pileDataAll['PileA1':'PileC3'][z].replace(" Dia Bore Pile",""))

        #Extracting Pile-Pile Spacings
        A_SpacingArray = pileDataAll.iloc[6:5+pileDataAll.loc['NoA']]
        C_SpacingArray = pileDataAll.iloc[24:23+pileDataAll.loc['NoC']]

        C_HorSpacingArray = pileDataAll.iloc[27:27+pileDataAll.loc['NoC']]

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        #Coordinates of A1 Pile
        CCX_current = CCX_origin - np.cos(np.deg2rad(theta))*pileDataAll.loc['AX']
        CCY_current = CCY_origin - np.sin(np.deg2rad(theta))*pileDataAll.loc['AX']

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.loc['PileA1']]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        #Coordinates of A2 Pile
        CCX_current = CCX_origin - np.sin(np.deg2rad(theta))*A_SpacingArray[0]
        CCY_current = CCY_origin + np.cos(np.deg2rad(theta))*A_SpacingArray[0]

        CCX_current2 = CCX_current - np.cos(np.deg2rad(theta))*pileDataAll.loc['AY']
        CCY_current2 = CCY_current - np.sin(np.deg2rad(theta))*pileDataAll.loc['AY']

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current2,CCY_current2,pileDataAll.loc['PileA2']]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(1,numberAPiles-1):
            CCX_current = CCX_current - A_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current + A_SpacingArray[y]*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[35+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberCPiles > 0:
            CCX_current = CCX_origin+pileDataAll.loc['CX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['C0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin+pileDataAll.loc['CX']*np.sin(np.deg2rad(theta))+pileDataAll.loc['C0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberCPiles):
                CCX_current = CCX_current - C_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) - (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + C_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==8:
        #Pin-shaped Pile Cap

        #Extracting Pile Cap Group datas
        pileDataAll = dataPlot.iloc[x,:]

        numberAPiles = pileDataAll.loc['NoA']
        numberBPiles = pileDataAll.loc['NoB']
        numberCPiles = pileDataAll.loc['NoC']

        numberPiles = numberAPiles + numberBPiles + numberCPiles

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        #Converting Pile Diameter
        for z in range(12):
            if "Dia" in pileDataAll.iloc[34+z]:
                pileDataAll.iloc[34+z] = int(pileDataAll['PileA1':'PileC3'][z].replace(" Dia Bore Pile",""))

        #Extracting Pile-Pile Spacings
        A_SpacingArray = pileDataAll.iloc[6:5+pileDataAll.loc['NoA']]
        B_SpacingArray = pileDataAll.iloc[15:14+pileDataAll.loc['NoB']]
        C_SpacingArray = pileDataAll.iloc[24:23+pileDataAll.loc['NoC']]

        B_HorSpacingArray = pileDataAll.iloc[19:19+pileDataAll.loc['NoB']]
        C_HorSpacingArray = pileDataAll.iloc[27:27+pileDataAll.loc['NoC']]

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        CCX_current = CCX_origin
        CCY_current = CCY_origin

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_origin,CCY_origin,pileDataAll.loc['PileA1']]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberAPiles-1):
            CCX_current = CCX_current - A_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current + A_SpacingArray[y]*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[35+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberBPiles > 0:
            CCX_current = CCX_origin-pileDataAll.loc['BX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['B0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin-pileDataAll.loc['BX']*np.sin(np.deg2rad(theta))-pileDataAll.loc['B0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[40]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberBPiles):
                CCX_current = CCX_current - B_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) + (B_HorSpacingArray[y]-B_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + B_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (B_HorSpacingArray[y]-B_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[40+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberCPiles > 0:
            CCX_current = CCX_origin+pileDataAll.loc['CX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['C0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin+pileDataAll.loc['CX']*np.sin(np.deg2rad(theta))+pileDataAll.loc['C0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberCPiles):
                CCX_current = CCX_current - C_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) - (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + C_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==9:
        #Key-shaped Pile Cap

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        numberAPiles = pileDataAll.loc['NoA']
        numberBPiles = pileDataAll.loc['NoB']
        numberCPiles = pileDataAll.loc['NoC']

        if numberBPiles == 2:
            pileDataAll.loc['B1']=pileDataAll.loc['B2']

        numberPiles = numberAPiles + numberBPiles + numberCPiles

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        #Converting Pile Diameter
        for z in range(12):
            if "Dia" in pileDataAll.iloc[34+z]:
                pileDataAll.iloc[34+z] = int(pileDataAll['PileA1':'PileC3'][z].replace(" Dia Bore Pile",""))

        #Extracting Pile-Pile Spacings
        A_SpacingArray = pileDataAll.iloc[6:5+pileDataAll.loc['NoA']]
        B_SpacingArray = pileDataAll.iloc[15:14+pileDataAll.loc['NoB']]
        C_SpacingArray = pileDataAll.iloc[24:23+pileDataAll.loc['NoC']]

        B_HorSpacingArray = pileDataAll.iloc[19:19+pileDataAll.loc['NoB']]
        C_HorSpacingArray = pileDataAll.iloc[27:27+pileDataAll.loc['NoC']]

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        CCX_current = CCX_origin
        CCY_current = CCY_origin

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_origin,CCY_origin,pileDataAll.loc['PileA1']]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberAPiles-1):
            CCX_current = CCX_current - A_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current + A_SpacingArray[y]*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[35+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberBPiles > 0:
            CCX_current = CCX_origin-pileDataAll.loc['BX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['B0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin-pileDataAll.loc['BX']*np.sin(np.deg2rad(theta))-pileDataAll.loc['B0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[40]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberBPiles):
                CCX_current = CCX_current - B_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) + (B_HorSpacingArray[y]-B_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + B_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (B_HorSpacingArray[y]-B_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[40+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberCPiles > 0:
            CCX_current = CCX_origin+pileDataAll.loc['CX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['C0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin+pileDataAll.loc['CX']*np.sin(np.deg2rad(theta))+pileDataAll.loc['C0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberCPiles):
                CCX_current = CCX_current - C_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) - (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + C_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)

    elif dataPlot.FID[x]==10:
        #E-shaped Pile Cap

        #Extracting Pile Cap Group data
        pileDataAll = dataPlot.iloc[x,:]

        numberAPiles = pileDataAll.loc['NoA']
        numberBPiles = pileDataAll.loc['NoB']
        numberCPiles = pileDataAll.loc['NoC']

        numberPiles = numberAPiles + numberBPiles + numberCPiles

        pileCounter = pileCounter + numberPiles

        #Extracting Pile Cap Marking and Pile Diameter
        pcMarking = pileDataAll.loc['PCMarking']

        theta = pileDataAll.loc['RotAngle'][:-1]
        theta = round(float(theta),2)

        #Converting Pile Diameter
        for z in range(12):
            if "Dia" in pileDataAll.iloc[34+z]:
                pileDataAll.iloc[34+z] = int(pileDataAll['PileA1':'PileC3'][z].replace(" Dia Bore Pile",""))

        #Extracting Pile-Pile Spacings
        A_SpacingArray = pileDataAll.iloc[6:5+pileDataAll.loc['NoA']]
        B_SpacingArray = pileDataAll.iloc[15:14+pileDataAll.loc['NoB']]
        C_SpacingArray = pileDataAll.iloc[24:23+pileDataAll.loc['NoC']]

        B_HorSpacingArray = pileDataAll.iloc[19:19+pileDataAll.loc['NoB']]
        C_HorSpacingArray = pileDataAll.iloc[27:27+pileDataAll.loc['NoC']]

        CCX_origin = dataPlot.iloc[x,3]
        CCY_origin = dataPlot.iloc[x,4]

        CCX_current = CCX_origin
        CCY_current = CCY_origin

        pileInvData = pd.DataFrame(data=[[pcMarking,CCX_origin,CCY_origin,pileDataAll.loc['PileA1']]],columns = ['PCMarking','CCX','CCY','sgdia'])
        pileInv = pileInv.append(pileInvData,ignore_index=True)

        for y in range(numberAPiles-1):
            CCX_current = CCX_current - A_SpacingArray[y]*np.sin(np.deg2rad(theta))
            CCY_current = CCY_current + A_SpacingArray[y]*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[35+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberBPiles > 0:
            CCX_current = CCX_origin-pileDataAll.loc['BX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['B0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin-pileDataAll.loc['BX']*np.sin(np.deg2rad(theta))-pileDataAll.loc['B0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[40]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberBPiles):
                CCX_current = CCX_current - B_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) + (B_HorSpacingArray[y]-B_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + B_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (B_HorSpacingArray[y]-B_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[40+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)

        if numberCPiles > 0:
            CCX_current = CCX_origin+pileDataAll.loc['CX']*np.cos(np.deg2rad(theta))-pileDataAll.loc['C0']*np.sin(np.deg2rad(theta))
            CCY_current = CCY_origin+pileDataAll.loc['CX']*np.sin(np.deg2rad(theta))+pileDataAll.loc['C0']*np.cos(np.deg2rad(theta))
            pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43]]],columns= ['PCMarking','CCX','CCY','sgdia'])
            pileInv = pileInv.append(pileInvData,ignore_index=True)

            for y in range(1, numberCPiles):
                CCX_current = CCX_current - C_SpacingArray[y-1]*np.sin(np.deg2rad(theta)) - (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.cos(np.deg2rad(theta))
                CCY_current = CCY_current + C_SpacingArray[y-1]*np.cos(np.deg2rad(theta)) + (C_HorSpacingArray[y]-C_HorSpacingArray[y-1])*np.sin(np.deg2rad(theta))
                pileInvData = pd.DataFrame(data=[[pcMarking,CCX_current,CCY_current,pileDataAll.iloc[43+y]]],columns= ['PCMarking','CCX','CCY','sgdia'])
                pileInv = pileInv.append(pileInvData,ignore_index=True)


# In[7]:


#COMPUTATION OF PILE-PILE SPACING

#Sorting of Pile Inventory based on position from a reference point
refPoint = np.array([pileInv.iloc[0].loc['CCX'],pileInv.iloc[0].loc['CCY']])
dist=[]

for x in range(pileInv.shape[0]):
    pilePoint = np.array([pileInv.iloc[x].loc['CCX'],pileInv.iloc[x].loc['CCY']])
    dist.append(np.linalg.norm(pilePoint - refPoint))

pileInv['dist_rel']=dist

pileInv = pileInv.sort_values(by=['dist_rel','CCY','CCX'])
pileInv = pileInv.reset_index(drop=True)

exceedList = pd.DataFrame(columns=['PileCap1','PileCap2','Limit','Actual'])

psLimit = float(input("Enter minimum pile spacing here (Diameters): "))


# In[8]:


for x in range(pileCounter-10):
    for y in range(1,10):
        diaControl = min(pileInv.iloc[x].loc['sgdia'],pileInv.iloc[x+y].loc['sgdia'])
        distLimit = diaControl*psLimit
        basePoint = np.array([pileInv.iloc[x].loc['CCX'],pileInv.iloc[x].loc['CCY']])
        measurePoint = np.array([pileInv.iloc[x+y].loc['CCX'],pileInv.iloc[x+y].loc['CCY']])
        measuredDistance = np.linalg.norm(measurePoint - basePoint)

        if measuredDistance < distLimit:
            exceedPile1 = pileInv.iloc[x].loc['PCMarking']
            exceedPile2 = pileInv.iloc[x+y].loc['PCMarking']
            exceedPileDF = pd.DataFrame([[exceedPile1,exceedPile2,distLimit,measuredDistance,pileInv.iloc[x].loc['CCX'],pileInv.iloc[x].loc['CCY'],pileInv.iloc[x+y].loc['CCX'],pileInv.iloc[x+y].loc['CCY']]],columns = ['PileCap1','PileCap2','Limit','Actual','BaseX','BaseY','PointX','PointY'])
            exceedList = exceedList.append(exceedPileDF,ignore_index=True,sort = False)

print(exceedList)
