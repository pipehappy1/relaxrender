from math import *


def loop(vertices,faces):
    '''
    input:vertices=[[x0,y0,z0],[x1,y1,z1]...],faces=[[index0,index1,index2]...]
    output:new_vertices,new_face
    '''
    num_faces=len(faces)
    num_vertices=len(vertices)
    new_vertices=vertices+[[0,0,0]]*num_faces*3
    new_index_of_ver=num_vertices
    edge_vertices=[]
    new_faces=[]

    for i in range(num_vertices):
        x=[]
        for j in range(num_vertices):
            x.append([0,0,0])
        edge_vertices.append(x)

    for f_i in range(0,num_faces):
        va=faces[f_i][0]
        vb=faces[f_i][1]
        vc=faces[f_i][2]
        vp,va,vb,vc,ev0,ev1,ev2,new_index_of_ver=add_edge_vertices(va,vb,vc,edge_vertices,new_index_of_ver)
        edge_vertices[va][vb][0]=ev0
        edge_vertices[va][vb][1]=ev1
        edge_vertices[va][vb][2]=ev2
        vq,va,vb,vc,ev0,ev1,ev2,new_index_of_ver=add_edge_vertices(vb,vc,va,edge_vertices,new_index_of_ver)
        edge_vertices[va][vb][0]=ev0
        edge_vertices[va][vb][1]=ev1
        edge_vertices[va][vb][2]=ev2
        vr,va,vb,vc,ev0,ev1,ev2,new_index_of_ver=add_edge_vertices(va,vc,vb,edge_vertices,new_index_of_ver)
        edge_vertices[va][vb][0]=ev0
        edge_vertices[va][vb][1]=ev1
        edge_vertices[va][vb][2]=ev2
        four_faces=[[va,vp,vr],[vp,vb,vq],[vr,vq,vc],[vr,vp,vq]]
        new_faces=new_faces+four_faces


    for v_i in range(0,num_vertices-1):
        for v_j in range(v_i,num_vertices):
            v_index=edge_vertices[v_i][v_j][0]
            if(v_index!=0):
                first_opposite_index_ver=edge_vertices[v_i][v_j][1]
                second_opposite_index_ver=edge_vertices[v_i][v_j][2]
                if(first_opposite_index_ver==0 or second_opposite_index_ver==0):
                    new_vertices[v_index]=[1.0/2*vertices[v_i][i]+1.0/2*vertices[v_j][i] for i in range(3)]
                else:
                    new_vertices[v_index]= [(3/8*vertices[v_i][i]+3/8*vertices[v_j][i] \
                    + 1/8*vertices[first_opposite_index_ver][i]+1/8*vertices[second_opposite_index_ver][i]) \
                     for i in range(3)]  
    
    adj_ver=[]
    for ov_i in range(0,num_vertices):
        x=[]
        for ov_j in range(0,num_vertices):   
            if((ov_i<ov_j and edge_vertices[ov_i][ov_j][0]!=0) or (ov_i>ov_j and edge_vertices[ov_j][ov_i][0]!=0)):
                x.append(ov_j)
        adj_ver.append(x)

    for ov in range (0,num_vertices):
        k=len(adj_ver[ov])
        adj_boundary_ver=[]
        for i in range(0,k):
            ov_adj=adj_ver[ov][i]
            if((ov_adj>ov and edge_vertices[ov][ov_adj][2]==0) or (ov_adj<ov and edge_vertices[ov_adj][ov][2]==0)):
                adj_boundary_ver.append(ov_adj)
        
        if(len(adj_boundary_ver)==2):
            new_vertices[ov]=[3/4*vertices[ov][i]+1/8*vertices[adj_boundary_ver[0]][i]\
            +1/8*vertices[adj_boundary_ver[1]][i] for i in range(3)]
        else:
            beta = 1/k*( 5/8 - (3/8 + 1/4*cos(2*pi/k))**2 )  
            new_vertices[ov]=[((1-k*beta)*vertices[ov][j] + beta*(sum(vertices[i][j] for i in adj_ver[ov]))) for j in range(3)]

    return new_vertices,new_faces

def add_edge_vertices(va,vb,vc,edge_vertices,new_index_of_ver):
    if (va>vb): 
        v_tmp = va  
        va = vb  
        vb = v_tmp  
    
    edge_vertices_va_vb_0=edge_vertices[va][vb][0]
    edge_vertices_va_vb_1=edge_vertices[va][vb][1]
    edge_vertices_va_vb_2=edge_vertices[va][vb][2]
    if (edge_vertices_va_vb_0==0):  
        edge_vertices_va_vb_0 = new_index_of_ver 
        edge_vertices_va_vb_1 = vc  
        new_index_of_ver = new_index_of_ver+1
    else:
        edge_vertices_va_vb_2 = vc
  
    new_ver_index = edge_vertices_va_vb_0
    return new_ver_index,va,vb,vc,edge_vertices_va_vb_0,edge_vertices_va_vb_1,edge_vertices_va_vb_2,new_index_of_ver
