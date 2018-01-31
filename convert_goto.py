import os
import re
jvs_file=os.path.abspath(r'C:\Users\Lin\Documents\GitHub\pet-store\inventory-service\src\main\java\com\xb\petstore\inventory\controller\InventoryController.java')

class goto_converter(object):
    def read_jvs(self):
        lines=[]
        is_goto_converted_needed=False
        with open(jvs_file,'r') as file_handle:
            lines=file_handle.readlines();
            goto_label=None
            dowhile_start = '\n\tProcess:\n\tdo {\n'
            dowhile_end='}while(false);//converted from AVS goto'
            main_execute_start_line_number=0
            for line_number,a_line in enumerate(lines):
                if(re.search(r'IContainerContext\scontext',a_line)):
                    main_execute_start_line_number=line_number

                    print('detected execute main method at '+ str(line_number))
                if(re.search(r'goto\s+\w+\s*;',a_line)):
                    is_goto_converted_needed=True
                    goto_label=re.search(r'goto\s+(\w+)\s*;',a_line)[1]
                    print('detected a goto '+goto_label+' at '+str(line_number)+' rewrite needed!')
                    lines[line_number]=re.sub(r'goto\s+\w+\s*;','break Process;//converted from AVS goto',a_line)
                if goto_label and (re.search(goto_label+r'\s*:',a_line)):
                    goto_section_start_line_number=line_number
                    print('detected goto section at ,'+str(line_number)+' rewriting using do while false')
                    lines[line_number] =re.sub(goto_label+r'\s*:',dowhile_end,a_line)
                    lines.insert(main_execute_start_line_number + 1, dowhile_start)


            # print('.'.join(lines))
        if is_goto_converted_needed:
            with open(jvs_file,'w') as file_writer:
                file_writer.writelines(lines)
                file_writer.flush()




if __name__ == '__main__':
    worker = goto_converter()
    worker.read_jvs()
