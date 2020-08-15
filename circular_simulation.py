import bpy,math
ob=bpy.data.objects["Sphere"]

li=[bpy.data.objects["Sphere.001"],bpy.data.objects["Sphere.002"],bpy.data.objects["Sphere.003"],bpy.data.objects["Sphere.004"],bpy.data.objects["Sphere.005"],bpy.data.objects["Sphere.006"]
,bpy.data.objects["Sphere.007"],bpy.data.objects["Sphere.008"],bpy.data.objects["Sphere.009"],bpy.data.objects["Sphere.010"],bpy.data.objects["Sphere.011"],bpy.data.objects["Sphere.012"]]


x,y=0,0
frame=0
i=0
t=0
def ref_sphere(sp,x,y):
    sp.location[0]=x
    sp.location[1]=y
    sp.keyframe_insert(data_path="location")
def sphere(sp,x1,y1,x2,y2):
    global x,y
    #x,y=dx,dy
    dx,dy=math.cos(x),math.sin(y)
    dx,dy=round(dx,2),round(dy,2)
    print(dx,dy)
    if (x1-0.05<dx<x1+0.05 and y1-0.05<dy<y1+0.05) or (x2-0.05<dx<x2+0.05 and y2-0.05<dy<y2+0.05):
        print("hello",y1-0.01,dy,y1+0.01)
        sp.location[0]=dx
        sp.location[1]=dy
        sp.keyframe_insert(data_path="location")


while i<200:
    
    
    bpy.context.scene.frame_set(frame)
    ref_sphere(ob,math.cos(x),math.sin(y))
    sphere(li[0],1,0,-1.0 ,0.04)
    sphere(li[1],0.97,0.21,-0.98 ,-0.17)
    sphere(li[2],0.87,0.47,-0.89 ,-0.44)
    sphere(li[3],0.69,0.71,-0.72 ,-0.68)
    sphere(li[4],0.45,0.89,-0.49 ,-0.87)
    sphere(li[5],0.26,0.96,-0.30 ,-0.95)
    sphere(li[6],-0.02,0.99,-0.01 ,-0.99)
    sphere(li[7],-0.22,0.97,0.28 ,-0.95)
    sphere(li[8],-0.5,0.86,0.55 ,-0.83)
    sphere(li[9],-0.73,0.67,0.70 ,-0.70)
    sphere(li[10],-0.85,0.51,0.88 ,-0.46)
    sphere(li[11],-0.97,0.23,0.96 ,-0.27)
    x+=0.1
    y+=0.1
    frame+=1
    i+=1