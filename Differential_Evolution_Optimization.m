disp('PROGRAM TO OPTIMIZE BURST PRESSURE FACTOR');
    clc;
    format long;
    close all;
    clear all;
tic
data=xlsread('C:\hieu 2016\Research\burst pressure\Pibul.xls');
Ymean=sum(data(:,9))/24;
for i=1:24 
ST(i,1)=data(i,9)^2-Ymean;
end
SST=sum(ST);
% ================Step 1: CREATE THE FIRST GENERATION================
    Np=0; 
    Start=[];
    while Np<30 % Number of quan the
    X1=random('unif',-5,0,1); %BETA 1
    X2=random('unif',0,5,1); %BETA 2
    X3=random('unif',-1,1,1); %BETA 3
  
[Result]=Pibula(X1,X2,X3,data);
         Np=Np+1;
        Start(Np,1)=X1;
        Start(Np,2)=X2;
        Start(Np,3)=X3;
        Start(Np,6)=Result;
        Start(Np,7)=1-Result/SST;


%     if Result>=1
%         Np=Np+1;
%         Start(Np,1)=X1;
%         Start(Np,2)=X2;
%         Start(Np,3)=pi()*X2^2/4-pi()*(X2-X1*2)^2/4; % Section Area - becareful
%         Start(Np,4)=pop;
%     end
    end
    Start
%     Area(1,:)=Start(:,3);
% 
     eps=0.001;
    Gmin=min(Start(:,6));   
     for i=1:Np
         if Start(i,6)==Gmin
         toiuu(1,:)=Start(1,:);
         end
     end
         
     GenerationNo=1;
     % ================Step 2: Create mutation================
while abs((abs(Gmin)-abs(sum(Start(:,6))/size(Start,1))))>eps
    %while and(abs((abs(Gmin)-abs(sum(Start(:,6))/size(Start,1))))>eps,GenerationNo<250) 
     F=0.75; %hang so dot bien
     V=[];
     j=1;
     while j<=Np  
         
     r1=random('unid',Np,1);
     r2=random('unid',Np,1);
     r3=random('unid',Np,1);
%      while or(r1==r2,(or(r1==r3,r2==r3)))
%      r1=random('unid',Np,1);
%     r2=random('unid',Np,1);
%     r3=random('unid',Np,1);
%      end
    
    r4=random('unid',Np,1);
    r5=random('unid',Np,1);
    r6=random('unid',Np,1);
%     while or(r4==r5,(or(r4==r6,r5==r6)))
%     r4=random('unid',Np,1);
%     r5=random('unid',Np,1);
%     r6=random('unid',Np,1);
%     end
    
    r7=random('unid',Np,1);
    r8=random('unid',Np,1);
    r9=random('unid',Np,1);
%     while or(r7==r8,(or(r7==r9,r8==r9)))
%     r7=random('unid',Np,1);
%     r8=random('unid',Np,1);
%     r9=random('unid',Np,1);
%     end
    
    
    X1=Start(r1,1)+F*(Start(r2,1)-Start(r3,1));
    X2=Start(r4,2)+F*(Start(r5,2)-Start(r6,2));
    X3=Start(r7,3)+F*(Start(r8,3)-Start(r9,3));
  
    [Result]=Pibula(X1,X2,X3,data);
%if 1+X2*data(i,9)^2/(data(i,2)*data(i,3))>=0
% if X3>0
        V(j,1)=X1;
        V(j,2)=X2;
        V(j,3)=X3;
        V(j,6)=Result;
        V(j,7)=1-Result/SST;
        
    j=j+1;
%      end

    end
%     end

    
    % ================Step 3: Lai ghep================
    Cr=1; %Xac suat lai ghep
    U=[];
    for i=1:Np
        rand=random('unif',0,1,1);
        if rand<Cr
            U(i,:)=V(i,:);
        else
            U(i,:)=Start(i,:);
        end
    end

    % ================Buoc 4: Lua chon================
    
    for i=1:Np
        if U(i,6)<=Start(i,6)
           Y(i,:)=U(i,:);
        else
           Y(i,:)=Start(i,:);
        end
    end
    
        % ================Buoc 5: Tai sinh================
    Start=Y;
    Gmin=min(Start(:,6))
     thehe(:,GenerationNo)=Start(:,7);
   GenerationNo=GenerationNo+1  
   Area(GenerationNo,:)=Start(:,6);
    for ii=1:Np
        if Start(ii,6)==Gmin
        toiuu(GenerationNo,:)=Start(ii,:);
        end
    end
   
   end
      for i=1:Np
       if Start(i,6)==Gmin
           Solution=Start(i,:);
           
       end
      end
%   toiuu
   Solution
toc
% 
% 
% figure
% title(sprintf('AREA OF CROSS SECTION'))
% grid on
% %set(gca,'XDir','normal','YDir','reverse');
% %set(gca,'YScale','Log');
% %line([0 50],[0.95 0.95])
% xlabel ('Generations');
% ylabel ('Acs (mm2)');
%  xlim ([0 GenerationNo+10]);
% % ylim ([0.9 1]);
% hold on
% plot(Area,'--rs','Color','white','MarkerEdgeColor','black','MarkerFaceColor','white','MarkerSize',3.5)
    %========================================
    
    
    
    
    
    
    
    
    
    
    
    