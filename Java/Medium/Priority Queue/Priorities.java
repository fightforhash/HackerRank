/*
 * Create the Student and Priorities classes here.
 */
import java.util.*;
class Student implements Comparable<Student>{
    String name = new String();
    double cgpa;
    int id;
    public Student(String name, double cgpa, int id){
        this.name = name;
        this.cgpa = cgpa;
        this.id = id;    
    }
    public String getName(){
        return this.name;
    }
    public double getCgpa(){
        return cgpa;
    }
    public int compareTo(Student student){
    double diffCGPA = student.cgpa - this.cgpa;
    if (diffCGPA == 0D){
        if (student.name.equals(this.name)){
            return student.id - this.id;
        }else{
            return this.name.compareTo(student.name);
        }
    }else{
            return diffCGPA < 0 ? -1:1;
        }
    
    
    }
    }
    class Priorities{
        List<Student> getStudents(List<String> events){
            PriorityQueue<Student> pq = new PriorityQueue<>();
            
            List<Student> res = new ArrayList();
            String [] vals;
            String name;
            double cgpa;
            int id;
            
            for (String e : events){
                vals = e.split(" ");
                if (vals.length ==4){
                    name = vals[1];
                    cgpa = Double.parseDouble(vals[2]);
                    id = Integer.parseInt(vals[3]);
                    
                    pq.add(new Student(name,cgpa,id));
                }else{
                    pq.poll();
                }
            }
            while(!pq.isEmpty()){
                res.add(pq.poll());
            }
            return res;
 
        }
    }
    
    
