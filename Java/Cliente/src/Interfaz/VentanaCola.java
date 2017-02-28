package Interfaz;

import PythonConexion.PythonConexion;
import javax.swing.JOptionPane;

/**
 *
 * @author moramaz
 */
public class VentanaCola extends javax.swing.JFrame {

    private final PythonConexion conexion;
    
    public VentanaCola(PythonConexion conexion) {
        initComponents();
        setLocationRelativeTo(null);
        this.conexion = conexion;
    }
    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        txtEnqueue = new javax.swing.JTextField();
        btnEnqueue = new javax.swing.JButton();
        btnDequeue = new javax.swing.JButton();

        btnEnqueue.setText("Enqueue");
        btnEnqueue.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEnqueueActionPerformed(evt);
            }
        });

        btnDequeue.setText("Dequeue");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(41, Short.MAX_VALUE)
                .addComponent(txtEnqueue, javax.swing.GroupLayout.PREFERRED_SIZE, 244, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(25, 25, 25))
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(btnEnqueue, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(btnDequeue, javax.swing.GroupLayout.DEFAULT_SIZE, 88, Short.MAX_VALUE))
                .addGap(0, 0, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(147, Short.MAX_VALUE)
                .addComponent(txtEnqueue, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnEnqueue)
                .addGap(31, 31, 31)
                .addComponent(btnDequeue)
                .addGap(130, 130, 130))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnEnqueueActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEnqueueActionPerformed
        if(txtEnqueue.getText().matches("\\d+")){
            conexion.queue_add(Integer.parseInt(txtEnqueue.getText()));
            txtEnqueue.setText("");
        }else{
            JOptionPane.showMessageDialog(this, "Sólo se pueden ingresar números.");
        }
    }//GEN-LAST:event_btnEnqueueActionPerformed

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnDequeue;
    private javax.swing.JButton btnEnqueue;
    private javax.swing.JTextField txtEnqueue;
    // End of variables declaration//GEN-END:variables
}