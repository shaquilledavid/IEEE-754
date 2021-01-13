import javax.swing.*;
import java.awt.*;
import javax.swing.SpringLayout;

class gui{
    public static void main(String args[]){
        JFrame frame = new JFrame("IEEE GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600,300);

        JPanel header = new JPanel();
        JLabel label = new JLabel("Enter Value");
        JTextField input = new JTextField(10);
        JButton encode = new JButton("Encode");
        JButton decode = new JButton("Decode");
        header.add(label);
        header.add(input);
        header.add(encode);
        header.add(decode);

        JPanel output = new JPanel(new SpringLayout());

        BoxLayout boxlayout = new BoxLayout(output, BoxLayout.PAGE_AXIS);
        output.setLayout(boxlayout);

        JLabel binary = new JLabel("Binary: ");
        output.add(binary);
        JTextField out_binary = new JTextField(10);
        binary.setLabelFor(out_binary);
        output.add(out_binary);

        JLabel binary_comp = new JLabel("Binary signed 2's complement: ");
        output.add(binary_comp);
        JTextField out_binary_comp = new JTextField(10);
        binary.setLabelFor(out_binary_comp);
        output.add(out_binary_comp);

        JLabel hex = new JLabel("Hex Number: ");
        output.add(hex);
        JTextField out_hex = new JTextField(10);
        binary.setLabelFor(out_hex);
        output.add(out_hex);

        frame.getContentPane().add(BorderLayout.NORTH, header);
        frame.getContentPane().add(BorderLayout.CENTER, output);
        frame.setVisible(true);
    }
}